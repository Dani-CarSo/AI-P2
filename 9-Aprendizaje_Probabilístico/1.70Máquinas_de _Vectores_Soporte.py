#70
#Máquinas de Vectores Soporte (Núcleo)

import numpy as np
# Importa NumPy para cálculos numéricos

from sklearn.svm import SVC
# Importa el clasificador SVM con soporte para kernels

from sklearn.datasets import make_circles
# Genera datos no linealmente separables (círculos)

# -----------------------------
# CREACIÓN DE DATOS
# -----------------------------

X, y = make_circles(n_samples=100, noise=0.1, factor=0.5)
# Crea un dataset en forma de círculos (no lineal)

# -----------------------------
# MODELO SVM CON KERNEL
# -----------------------------

model = SVC(kernel="rbf", C=1.0, gamma="scale")
# SVM con kernel RBF (gaussiano)
# C controla penalización de errores
# gamma controla forma del kernel

# -----------------------------
# ENTRENAMIENTO
# -----------------------------

model.fit(X, y)
# Entrena el modelo con los datos

# -----------------------------
# FUNCIÓN DE PREDICCIÓN INTERACTIVA
# -----------------------------

def predict_point():
    # Permite clasificar un punto ingresado por el usuario
    
    x = float(input("Ingresa x: "))
    # Entrada coordenada x
    
    y_point = float(input("Ingresa y: "))
    # Entrada coordenada y
    
    point = np.array([[x, y_point]])
    # Convierte a formato de matriz
    
    prediction = model.predict(point)
    # Predice clase usando SVM con kernel
    
    print("\nResultado:")
    # Encabezado
    
    if prediction[0] == 0:
        # Clase 0
        
        print("Clase: 0 (círculo interno)")
    else:
        # Clase 1
        
        print("Clase: 1 (círculo externo)")

# -----------------------------
# INTERFAZ INTERACTIVA
# -----------------------------

print("=== SVM CON KERNEL (INTERACTIVO) ===")
# Título del programa

print("Este modelo separa datos NO lineales usando kernel RBF")
# Explicación del modelo

print("Escribe '1' para probar un punto o '0' para salir\n")
# Instrucciones

# -----------------------------
# LOOP PRINCIPAL
# -----------------------------

while True:
    # Bucle infinito hasta que el usuario salga
    
    option = input("Opción: ")
    # Entrada del usuario

    if option == "0":
        # Salir del programa
        break

    elif option == "1":
        # Clasificar un punto
        
        predict_point()
        # Llama función de predicción

    else:
        print("Opción inválida")
        # Manejo de error