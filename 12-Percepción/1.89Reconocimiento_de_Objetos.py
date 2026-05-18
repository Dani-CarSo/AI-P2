#89
#Reconocimientos de Objetos

import cv2  # Importamos OpenCV para visualizar los resultados

# 1. Cargamos el modelo pre-entrenado (n = nano, el más rápido y ligero)
# Este modelo ya sabe reconocer 80 clases de objetos comunes.
modelo = YOLO('yolov8n.pt')

# 2. Realizamos la detección sobre una imagen o video
# El parámetro 'save=True' guarda una copia de la imagen con los cuadros dibujados
resultados = modelo.predict('imagen_prueba.jpg', conf=0.5, save=True)

# 3. Iteramos sobre los resultados obtenidos
for resultado in resultados:
    # Imprimimos en consola qué objetos detectó y en qué coordenadas
    print(resultado.boxes) 
    
    # 4. Mostramos la imagen final procesada en una ventana de Windows/Linux/Mac
    imagen_renderizada = resultado.plot()  # Dibuja los cuadros y etiquetas sobre la imagen
    cv2.imshow('Deteccion de Objetos', imagen_renderizada)  # Abre la ventana visual
    
    # 5. Mantenemos la ventana abierta hasta que se presione una tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()  # Cerramos todas las ventanas al terminar