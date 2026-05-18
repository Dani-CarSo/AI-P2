#86
#Graficos por Computador

import pygame  # Importamos Pygame para gestionar la ventana y eventos
from pygame.locals import * # Importamos constantes para facilitar el código
from OpenGL.GL import * # Funciones principales de la librería gráfica OpenGL
from OpenGL.GLU import * # Funciones de utilidad de OpenGL para la cámara

# 1. Definimos los vértices (puntos en el espacio X, Y, Z) del cubo
vertices = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), # Cara trasera
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)      # Cara frontal
)

# 2. Definimos las aristas (líneas que conectan los vértices)
# Cada par representa los índices de los vértices que se unen
aristas = (
    (0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
    (6,3), (6,4), (6,7), (5,1), (5,4), (5,7)
)

def DibujarCubo():
    """Función para dibujar las líneas del cubo en el espacio 3D"""
    glBegin(GL_LINES)  # Indicamos que vamos a dibujar líneas
    for arista in aristas:
        for vertice in arista:
            glVertex3fv(vertices[vertice])  # Enviamos la coordenada al procesador gráfico
    glEnd()  # Finalizamos el dibujo

# 3. Inicialización de la ventana y el contexto gráfico
pygame.init()
display = (800, 600)  # Definimos el tamaño de la ventana
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # Activamos el soporte para OpenGL

# 4. Configuración de la "Cámara" (Perspectiva)
# Fov: 45 grados, Aspect Ratio, Near plane: 0.1, Far plane: 50.0
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)  # Movemos la cámara hacia atrás para ver el objeto

# 5. Bucle principal de renderizado
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si cerramos la ventana, termina el programa
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 1)  # Aplicamos una rotación constante en los ejes X, Y, Z
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpiamos la pantalla y el buffer de profundidad
    
    DibujarCubo()  # Llamamos a nuestra función de dibujo
    
    pygame.display.flip()  # Intercambiamos los buffers para mostrar el frame renderizado
    pygame.time.wait(10)  # Pequeña pausa para no saturar el procesador