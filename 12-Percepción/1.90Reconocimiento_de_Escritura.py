#90
#Reconocimiento de Escritura

import cv2  # Importamos OpenCV para el manejo y procesamiento de imágenes
import pytesseract  # Importamos la librería que conecta Python con el motor Tesseract

# Especificamos la ruta del ejecutable de Tesseract (necesario en Windows)
# Si estás en Linux o Mac, esta línea suele no ser necesaria.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Cargamos la imagen que contiene la escritura (manual o digital)
imagen = cv2.imread('nota_escrita.png')

# Convertimos la imagen a escala de grises para facilitar la lectura del motor
# El OCR funciona mejor si no tiene que lidiar con canales de color (RGB)
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicamos un umbral (threshold) para convertir la imagen a blanco y negro puro
# Esto ayuda a resaltar el texto y eliminar "ruido" o sombras del fondo
_, binarizacion = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Usamos Pytesseract para extraer el texto de la imagen procesada
# El parámetro lang='spa' le indica al motor que busque caracteres en español
texto_extraido = pytesseract.image_to_string(binarizacion, lang='spa')

# Mostramos el resultado final en la consola
print("--- Texto Detectado ---")
print(texto_extraido)

# (Opcional) Mostramos la imagen que el programa procesó para verificar la calidad
cv2.imshow('Imagen Procesada', binarizacion)
cv2.waitKey(0)  # Espera a que presiones una tecla para cerrar la ventana
cv2.destroyAllWindows()  # Limpia las ventanas abiertas de OpenCV