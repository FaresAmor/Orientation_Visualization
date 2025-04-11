import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import serial
import time
import math

# Initialisation de la liaison série
ser = serial.Serial('COM10', 115200)  # Change COM10 si nécessaire
time.sleep(2)

# Variables pour la fusion des données
alpha = 0.98  # Coefficient de filtre de complémentarité (ajustable)

# Variables pour stocker l'orientation
angle_x = 0.0
angle_y = 0.0
angle_z = 0.0

vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

faces = [
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
]

colors = [
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (1, 1, 0),  # Yellow
    (1, 0, 1),  # Magenta
    (0, 1, 1)   # Cyan
]

def draw_cube():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i])  # Apply a color to each face
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def read_mpu():
    try:
        line = ser.readline().decode().strip()
        parts = line.split(',')
        if len(parts) == 6:  # 3 axes pour l'accéléromètre et 3 pour le gyroscope
            ax = float(parts[0])
            ay = float(parts[1])
            az = float(parts[2])
            gx = float(parts[3])
            gy = float(parts[4])
            gz = float(parts[5])
            return ax, ay, az, gx, gy, gz
        else:
            print("Mauvais format reçu :", line)
            return 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    except Exception as e:
        print("Erreur de lecture :", e)
        return 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

def complementary_filter(acc_angle, gyro_rate, dt, alpha=0.98, angle_x=0.0, angle_y=0.0, angle_z=0.0):
    # Calculer l'angle à partir de l'accéléromètre (basé sur les axes X et Y)
    acc_angle_x = math.atan2(acc_angle[1], acc_angle[2]) * 180 / math.pi
    acc_angle_y = math.atan2(acc_angle[0], acc_angle[2]) * 180 / math.pi
    acc_angle_z = math.atan2(acc_angle[0], math.sqrt(acc_angle[1]**2 + acc_angle[2]**2)) * 180 / math.pi

    # Appliquer le filtre de complémentarité
    angle_x = alpha * (gyro_rate[0] * dt + angle_x) + (1 - alpha) * acc_angle_x
    angle_y = alpha * (gyro_rate[1] * dt + angle_y) + (1 - alpha) * acc_angle_y
    angle_z = alpha * (gyro_rate[2] * dt + angle_z) + (1 - alpha) * acc_angle_z

    return angle_x, angle_y, angle_z

def main():
    global angle_x, angle_y, angle_z

    pygame.init()
    display = (1000,800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    last_time = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ser.close()
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        ax, ay, az, gx, gy, gz = read_mpu()
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        # Fusion des données pour obtenir l'orientation
        angle_x, angle_y, angle_z = complementary_filter([ax, ay, az], [gx, gy, gz], dt, alpha, angle_x, angle_y, angle_z)

        glPushMatrix()

        # Appliquer les rotations
        glRotatef(angle_x, 1, 0, 0)  # Rotation autour de l'axe X
        glRotatef(angle_y, 0, 1, 0)  # Rotation autour de l'axe Y
        glRotatef(angle_z, 0, 0, 1)  # Rotation autour de l'axe Z

        draw_cube()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
