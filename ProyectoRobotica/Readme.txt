# Evaluación Cinemática y Dinámica de un Robot SCARA

**Autor:** Mauricio Dariel Torbellín Sanchez  
**Asignatura:** Robótica  
**Periodo:** 2026-1  

## 📄 Descripción del Proyecto
Este proyecto tiene como objetivo la evaluación integral de un manipulador robótico tipo SCARA. Se realizó un análisis teórico riguroso (Cinemática Inversa, Jacobiano, Dinámica Euler-Lagrange) para validar el seguimiento de una **trayectoria elíptica**.

Posteriormente, se implementó una simulación física en **ROS 2 Jazzy** y **Gazebo**, desarrollando un nodo de control en Python capaz de leer la trayectoria calculada y ejecutarla en el robot virtual.

## 📂 Contenido del Repositorio
Los archivos principales se encuentran en la carpeta `Proyecto_Final`:

* **`Proyecto_Evaluacion_Robot_Final.mlx`**: Script de MATLAB con el cálculo matemático, generación de gráficas (torque, potencia, manipulabilidad) y exportación de datos.
* **`trayectoria_scara.csv`**: Archivo de datos generado por MATLAB con los ángulos articulares calculados ($q_1, q_2, q_3$).
* **`reproducir_trayectoria.py`**: Nodo de ROS 2 (Python) que lee el CSV, controla el robot y visualiza la trayectoria en RViz.
* **`scara_urdf.xacro`**: Archivo de descripción del robot con las **inercias corregidas** para garantizar la estabilidad física en Gazebo.

## 🚀 Instrucciones de Ejecución

### 1. Requisitos
* ROS 2 Jazzy
* Gazebo Simulator
* Paquetes del repositorio compilados

### 2. Compilación (Importante)
Se incluye una corrección al modelo URDF. Para aplicarla:

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
3. Ejecutar Simulación

En una terminal, lanzar el entorno de Gazebo:
Bash

ros2 launch scara_bringup gz2_scara.launch.py

4. Ejecutar Nodo de Control

En una segunda terminal, ejecutar el script para reproducir la trayectoria elíptica:
Bash

cd ~/ros2_ws/src/robotica_2026-1/Proyecto_Final
python3 reproducir_trayectoria.py

🎥 Evidencia de Funcionamiento

En el siguiente video se demuestra la ejecución de la trayectoria, la visualización en RViz y el comportamiento dinámico del robot:
https://youtu.be/UkNp5Usdczg


