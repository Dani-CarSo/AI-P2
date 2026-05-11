#89
#Texturas y Sombras

import cv2  # Importamos la librería de visión por computadora
import numpy as np  # Importamos numpy para operaciones matemáticas sobre los píxeles

# 1. Cargamos la imagen original
imagen = cv2.imread('pared_o_suelo.jpg')

# 2. Convertimos a escala de grises
# Las texturas se definen por cambios de brillo, el color suele estorbar
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# --- DETECCIÓN DE TEXTURA (RELIEVE) ---
# Usamos el operador Sobel para calcular el gradiente (cambio de intensidad)
# Esto resalta las rugosidades y patrones de la superficie
sobel_x = cv2.Sobel(gris, cv2.CV_64F, 1, 0, ksize=3) # Detecta texturas verticales
sobel_y = cv2.Sobel(gris, cv2.CV_64F, 0, 1, ksize=3) # Detecta texturas horizontales
textura = cv2.magnitude(sobel_x, sobel_y) # Combina ambas para ver la textura total

# --- DETECCIÓN DE SOMBRAS ---
# Convertimos la imagen al espacio de color HSV (Matiz, Saturación, Valor)
# En este espacio, el canal 'V' (Value) representa el brillo puro
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
v_canal = hsv[:, :, 2] # Extraemos solo la capa de brillo

# Aplicamos un filtro para aislar las zonas muy oscuras (posibles sombras)
# Los píxeles con brillo menor a 50 se marcan como sombra (negro)
_, sombras = cv2.threshold(v_canal, 50, 255, cv2.THRESH_BINARY_INV)

# 3. Mostramos los resultados
cv2.imshow('Textura y Relieve', textura.astype(np.uint8)) # Mostramos la rugosidad
cv2.imshow('Mapa de Sombras', sombras) # Mostramos dónde el algoritmo cree que hay sombra
cv2.waitKey(0)
cv2.destroyAllWindows()