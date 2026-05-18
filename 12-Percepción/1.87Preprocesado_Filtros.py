#87
#Preprocesado: Filtros linea por linea

import cv2  # Importamos la librería de visión
import numpy as np  # Para crear matrices de filtros personalizadas

# 1. Cargamos la imagen original
imagen = cv2.imread('foto_con_ruido.jpg')

# --- FILTRO DE PROMEDIO (Blur) ---
# Toma un bloque de píxeles (5x5) y los promedia. Difumina todo por igual.
filtro_promedio = cv2.blur(imagen, (5, 5))

# --- FILTRO GAUSSIANO (Gaussian Blur) ---
# Es más natural: le da más peso a los píxeles centrales que a los de los bordes.
# Es el estándar para eliminar ruido antes de detectar aristas.
filtro_gaussiano = cv2.GaussianBlur(imagen, (5, 5), 0)

# --- FILTRO DE MEDIANA (Median Blur) ---
# Excelente para eliminar el ruido tipo "sal y pimienta" (puntos blancos y negros).
# No promedia, sino que elige el valor central de todos los píxeles del área.
filtro_mediana = cv2.medianBlur(imagen, 5)

# --- FILTRO BILATERAL ---
# El más avanzado: suaviza la imagen pero MANTIENE los bordes nítidos.
# Es ideal si quieres limpiar la imagen sin perder la forma de los objetos.
filtro_bilateral = cv2.bilateralFilter(imagen, 9, 75, 75)

# 2. Mostramos los resultados para comparar el efecto de cada uno
cv2.imshow('1. Original', imagen)
cv2.imshow('2. Promedio (Borrosidad uniforme)', filtro_promedio)
cv2.imshow('3. Gaussiano (Suavizado inteligente)', filtro_gaussiano)
cv2.imshow('4. Mediana (Elimina puntos)', filtro_mediana)
cv2.imshow('5. Bilateral (Limpia sin perder bordes)', filtro_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()