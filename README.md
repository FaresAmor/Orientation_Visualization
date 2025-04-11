# Orientation Visualization with MPU6500 and OpenGL

## Overview  
This project allows you to visualize the orientation of a 3D cube in real-time, using an **MPU6500** (accelerometer and gyroscope) sensor connected to an **ESP32**. The data is read via a serial communication and fused using a complementary filter to get an accurate estimate of the orientation angles. The 3D cube visualization is done using **Pygame** and **OpenGL**.

### Project Objective:
- Read real-time orientation data from the **MPU6500**.
- Fuse this data with a **complementary filter** to obtain more accurate tilt angles.
- Display a **3D cube** rotating according to the orientation measured by the sensor.

## Components Used  
- **Microcontroller:** ESP32  
- **Motion Sensor:** MPU6500 (accelerometer and gyroscope)  
- **Python Libraries:**
  - `pygame` for managing the graphical window  
  - `PyOpenGL` for 3D rendering  
  - `pySerial` for serial communication between ESP32 and the computer  
- **3D Cube:** A representation of a cube that rotates in real-time based on sensor data.

## Features  
✔️ **Real-time visualization** of a 3D cube rotating based on the orientation measured by the MPU6500 sensor.  
✔️ **Fusion of accelerometer and gyroscope data** to obtain a reliable estimate of tilt angles using a **complementary filter**.  
✔️ **Rotation around three axes (X, Y, Z)** to simulate the real orientation of the sensor in space.  
✔️ Display of **X, Y, Z rotation axes** for visual tracking of orientations.

## Files Included  
📁 **Project Files**:  
  - **main.py**: Main script to read sensor data and display the cube.  
  - **README.md**: This documentation file.  
  - **Wiring Diagrams** (optional, if applicable).  
  - **Source files** for ESP32 and MPU6500 sensor.

## Installation & Usage  
1. **Clone the project** from GitHub:  
   ```bash
   git clone https://github.com/your-username/project-name.git

## 📜 Wiring Diagram of MPU6500 Sensor and ESP32
![Image Alt](https://github.com/FaresAmor/HARDWARE-Design/blob/403708126704611446c14cd4ab31e6370bbe946b/Reg.png)

## 🖥️ 3D Cube Rotation View
![Image Alt](https://github.com/FaresAmor/HARDWARE-Design/blob/403708126704611446c14cd4ab31e6370bbe946b/Reg.png)



## Contribution
Feel free to explore, modify, and contribute! If you find any issues or improvements, open a pull request or raise an issue. 🚀




Feel free to explore, modify, and contribute! 🚀



