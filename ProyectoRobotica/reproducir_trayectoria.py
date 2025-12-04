#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import csv
import time
import os

class ScaraTrajectoryPlayer(Node):
    def __init__(self):
        super().__init__('scara_player')
        
        # Publicadores (Asegúrate que coinciden con tus topics)
        self.pub_j1 = self.create_publisher(Float64, '/joint1/cmd_pos', 10)
        self.pub_j2 = self.create_publisher(Float64, '/joint2/cmd_pos', 10)
        self.pub_j3 = self.create_publisher(Float64, '/joint3/cmd_pos', 10)
        
        self.get_logger().info('Inicializando nodo...')
        time.sleep(1) 

    def publish_joints(self, q1, q2, q3):
        msg = Float64()
        msg.data = float(q1)
        self.pub_j1.publish(msg)
        msg.data = float(q2)
        self.pub_j2.publish(msg)
        msg.data = float(q3)
        self.pub_j3.publish(msg)

    def play_csv(self, file_path):
        if not os.path.exists(file_path):
            self.get_logger().error('¡ARCHIVO NO ENCONTRADO!')
            return

        # 1. Cargar todos los puntos en memoria
        trajectory_points = []
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                try:
                    p = [float(row[0]), float(row[1]), float(row[2])]
                    trajectory_points.append(p)
                except ValueError:
                    pass
        
        if not trajectory_points:
            self.get_logger().error('El archivo CSV está vacío.')
            return

        # --- FASE 1: APROXIMACIÓN SUAVE (Evita el latigazo inicial) ---
        start_point = trajectory_points[0]
        self.get_logger().info(f'---> Yendo suavemente al inicio: {start_point}')
        
        # Enviamos el primer punto varias veces para dar tiempo a que llegue
        for _ in range(50):
            self.publish_joints(start_point[0], start_point[1], start_point[2])
            time.sleep(0.05) 
            
        self.get_logger().info('Posición inicial alcanzada. Esperando 1s...')
        time.sleep(1.0)

        # --- FASE 2: EJECUTAR LA ELIPSE ---
        self.get_logger().info('¡COMENZANDO TRAYECTORIA! 🎬')
        
        for i, point in enumerate(trajectory_points):
            self.publish_joints(point[0], point[1], point[2])
            
            if i % 100 == 0:
                self.get_logger().info(f'Punto {i}/{len(trajectory_points)}...')
            
            # Velocidad de reproducción (ajusta según necesites)
            time.sleep(0.01) 

        self.get_logger().info('--- FIN DE LA TRAYECTORIA ---')

def main(args=None):
    rclpy.init(args=args)
    player = ScaraTrajectoryPlayer()
    
    # Asegúrate que el CSV esté en la carpeta donde ejecutas la terminal
    csv_path = 'trayectoria_scara.csv' 
    
    player.play_csv(csv_path)
    player.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()