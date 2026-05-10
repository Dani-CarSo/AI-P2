#71
#Computación Neuronal


import numpy as np
# Librería para cálculos matemáticos

# -----------------------------
# Función de activación
# -----------------------------

def sigmoid(x):
    # Convierte valores a rango 0-1
    
    return 1 / (1 + np.exp(-x))
    # Función sigmoide

# -----------------------------
# Datos de entrenamiento simples (AND lógico)
# -----------------------------

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
# Entradas posibles

y = np.array([0, 0, 0, 1])
# Salidas esperadas (tabla AND)

# -----------------------------
# Inicialización de pesos
# -----------------------------

w = np.random.rand(2)
# Pesos aleatorios para 2 entradas

b = np.random.rand()
# Bias inicial aleatorio

lr = 0.1
# Tasa de aprendizaje

# -----------------------------
# Entrenamiento
# -----------------------------

for epoch in range(1000):
    # Repite muchas veces para aprender
    
    for i in range(len(X)):
        # Recorre cada muestra
        
        x = X[i]
        # Entrada actual
        
        y_true = y[i]
        # Valor real
        
        z = np.dot(x, w) + b
        # Suma ponderada
        
        y_pred = sigmoid(z)
        # Predicción de la neurona
        
        error = y_true - y_pred
        # Error de predicción
        
        # -------------------------
        # Ajuste de pesos
        # -------------------------
        
        w += lr * error * x
        # Ajusta pesos según error
        
        b += lr * error
        # Ajusta bias

# -----------------------------
# INTERACCIÓN
# -----------------------------

print("=== COMPUTACIÓN NEURONAL INTERACTIVA ===")
print("Ingresa dos valores (0 o 1)")

while True:
    
    x1 = input("x1 (o 'salir'): ")
    # Primera entrada
    
    if x1.lower() == "salir":
        break
    
    x2 = input("x2: ")
    # Segunda entrada
    
    x_input = np.array([float(x1), float(x2)])
    # Convierte a vector
    
    z = np.dot(x_input, w) + b
    # Suma ponderada
    
    output = sigmoid(z)
    # Salida de la neurona
    
    print(f"Salida neuronal: {output:.3f}")
    # Resultado
    
    if output > 0.5:
        print("Clase: 1")
    else:
        print("Clase: 0")