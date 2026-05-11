#90
#Detección de Aristas y Segmentación

import cv2  # Librería principal de visión por computadora
import numpy as np  # Para manejo de matrices y arreglos de píxeles

# 1. Cargamos la imagen desde el disco
imagen = cv2.imread('objeto_prueba.jpg')

# 2. Pre-procesamiento: Convertimos a gris y aplicamos desenfoque
# El desenfoque elimina el ruido para que el detector no vea "bordes falsos"
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
suavizado = cv2.GaussianBlur(gris, (5, 5), 0)

# --- DETECCIÓN DE ARISTAS (Canny) ---
# Canny busca cambios bruscos de intensidad. 
# 100 y 200 son los umbrales mínimo y máximo de sensibilidad.
aristas = cv2.Canny(suavizado, 100, 200)

# --- SEGMENTACIÓN (Thresholding / Umbralización) ---
# El método de Otsu calcula automáticamente el mejor punto de corte 
# para separar el objeto (blanco) del fondo (negro).
_, segmentada = cv2.threshold(suavizado, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# --- EXTRACCIÓN DE CONTORNOS ---
# Buscamos las líneas cerradas basadas en las aristas detectadas
contornos, _ = cv2.findContours(aristas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujamos los contornos encontrados sobre una copia de la imagen original
# (0, 255, 0) es color verde y el 2 es el grosor de la línea
imagen_contornos = imagen.copy()
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

# 3. Mostramos los tres pasos del proceso
cv2.imshow('1. Aristas (Canny)', aristas)
cv2.imshow('2. Segmentacion (Otsu)', segmentada)
cv2.imshow('3. Contornos Finales', imagen_contornos)

cv2.waitKey(0)
cv2.destroyAllWindows()