#42
#Redes Neuronales

import numpy as np  # librería para hacer operaciones matemáticas con matrices y arreglos

# DATOS 
# Cada fila es una flor con 4 medidas en cm:
# [largo_sépalo, ancho_sépalo, largo_pétalo, ancho_pétalo]

datos = np.array([          # creamos una matriz de 30 filas x 4 columnas
    # Setosa (clase 0)
    [5.1,3.5,1.4,0.2], [4.9,3.0,1.4,0.2], [4.7,3.2,1.3,0.2],
    [4.6,3.1,1.5,0.2], [5.0,3.6,1.4,0.2], [5.4,3.9,1.7,0.4],
    [4.6,3.4,1.4,0.3], [5.0,3.4,1.5,0.2], [4.4,2.9,1.4,0.2],
    [4.9,3.1,1.5,0.1],
    # Versicolor (clase 1)
    [7.0,3.2,4.7,1.4], [6.4,3.2,4.5,1.5], [6.9,3.1,4.9,1.5],
    [5.5,2.3,4.0,1.3], [6.5,2.8,4.6,1.5], [5.7,2.8,4.5,1.3],
    [6.3,3.3,4.7,1.6], [4.9,2.4,3.3,1.0], [6.6,2.9,4.6,1.3],
    [5.2,2.7,3.9,1.4],
    # Virginica (clase 2)
    [6.3,3.3,6.0,2.5], [5.8,2.7,5.1,1.9], [7.1,3.0,5.9,2.1],
    [6.3,2.9,5.6,1.8], [6.5,3.0,5.8,2.2], [7.6,3.0,6.6,2.1],
    [4.9,2.5,4.5,1.7], [7.3,2.9,6.3,1.8], [6.7,2.5,5.8,1.8],
    [7.2,3.6,6.1,2.5],
])

etiquetas = np.array([0]*10 + [1]*10 + [2]*10)
# arreglo de 30 números: [0,0,...,1,1,...,2,2,...]
# le dice a la red cuál es la respuesta correcta para cada flor

#  PREPROCESAMIENTO 
X = (datos - datos.min(axis=0)) / (datos.max(axis=0) - datos.min(axis=0))
# normalización: lleva todos los valores al rango [0, 1]
# sin esto, números grandes dominarían el entrenamiento y la red aprendería mal
# axis=0 significa "por columna", para normalizar cada medida por separado


def one_hot(etiquetas, n_clases=3):
    # convierte un número de clase en un vector de ceros con un solo 1
    # ej: clase 0 → [1,0,0]  /  clase 1 → [0,1,0]  /  clase 2 → [0,0,1]
    # esto permite que la red tenga 3 neuronas de salida, una por especie

    matriz = np.zeros((len(etiquetas), n_clases))  # crea matriz de puros ceros: (30, 3)
    for i, e in enumerate(etiquetas):              # recorre cada etiqueta con su índice
        matriz[i][e] = 1                           # pone un 1 en la posición de la clase correcta
    return matriz

Y = one_hot(etiquetas)  # Y tiene shape (30, 3) — respuestas esperadas en formato one-hot


#PESOS INICIALES
np.random.seed(0)  # fija la semilla aleatoria para que el resultado sea reproducible

pesos_1 = np.random.randn(4, 8) * 0.5
# matriz de pesos entre capa de entrada (4) y capa oculta (8)
# shape (4, 8): cada entrada se conecta con cada neurona oculta → 32 pesos en total
# se multiplica por 0.5 para que los valores iniciales sean pequeños y la red arranque estable

sesgo_1 = np.zeros((1, 8))
# bias (sesgo) para las 8 neuronas ocultas, arranca en 0
# el bias permite que la neurona se active incluso cuando todas las entradas son 0

pesos_2 = np.random.randn(8, 3) * 0.5
# pesos entre capa oculta (8) y capa de salida (3 clases)
# shape (8, 3): cada neurona oculta conectada con cada neurona de salida → 24 pesos

sesgo_2 = np.zeros((1, 3))
# bias para las 3 neuronas de salida


# FUNCIONES DE ACTIVACIÓN 

def relu(x):
    return np.maximum(0, x)
    # ReLU: si el valor es negativo devuelve 0, si no lo deja igual
    # ej: relu(-3) = 0  /  relu(5) = 5
    # se usa en la capa oculta para añadir no-linealidad sin saturarse como sigmoid

def relu_derivada(x):
    return (x > 0).astype(float)
    # derivada de ReLU: devuelve 1 donde x era positivo, 0 donde era negativo
    # se necesita en el backpropagation para calcular los gradientes

def softmax(x):
    e = np.exp(x - x.max(axis=1, keepdims=True))
    # se resta el máximo antes de elevar e para evitar números enormes (overflow)
    # ej: exp(1000) daría infinito, pero exp(1000-1000) = exp(0) = 1

    return e / e.sum(axis=1, keepdims=True)
    # divide cada valor entre la suma total → probabilidades que suman exactamente 1
    # ej: [2.1, 0.5, 0.3] → [0.72, 0.17, 0.11]


#ENTRENAMIENTO
lr     = 0.05   # tasa de aprendizaje: qué tan grandes son los pasos al ajustar pesos
epocas = 5000   # número de veces que la red verá todos los datos

print("Entrenando...\n")

for epoca in range(epocas):  # repite el ciclo completo 5000 veces

    # FORWARD PASS (la red hace su predicción)
    z1 = X @ pesos_1 + sesgo_1
    # @ es multiplicación de matrices
    # cada neurona oculta recibe la suma ponderada de todas las entradas + su bias
    # shape resultante: (30, 8) — un valor por neurona oculta por cada flor

    a1 = relu(z1)
    # aplica ReLU a cada neurona oculta
    # "activa" las neuronas: las que recibieron señal positiva pasan, las negativas se apagan

    z2 = a1 @ pesos_2 + sesgo_2
    # multiplica las activaciones ocultas por los pesos de la capa 2
    # shape resultante: (30, 3) — un valor por clase por cada flor

    a2 = softmax(z2)
    # convierte los valores finales en probabilidades
    # ej para una flor: [0.02, 0.95, 0.03] → la red cree 95% que es Versicolor

    # PÉRDIDA (qué tan equivocada está la red) 
    perdida = -np.mean(Y * np.log(a2 + 1e-9))

    # BACKPROPAGATION (calcular cuánto ajustar cada peso)
    d2 = (a2 - Y) / len(X)
    # gradiente de la capa de salida: diferencia entre lo predicho y lo esperado
    # dividido entre len(X)=30 para promediar el error sobre todos los ejemplos

    d1 = (d2 @ pesos_2.T) * relu_derivada(z1)
    # gradiente de la capa oculta: propaga el error hacia atrás por los pesos
    # pesos_2.T es la transpuesta — "invierte" la dirección del flujo de error
    # se multiplica por relu_derivada para ignorar neuronas que estaban apagadas (=0)

    # ACTUALIZAR PESOS (descenso de gradiente)
    pesos_2 -= a1.T @ d2 * lr
    # ajusta los pesos de la capa 2 en la dirección que reduce el error
    # -= significa: nuevo_peso = peso_actual - (gradiente × tasa_de_aprendizaje)

    sesgo_2 -= d2.sum(axis=0, keepdims=True) * lr
    # ajusta el bias de la capa 2 — suma los gradientes de todos los ejemplos

    pesos_1 -= X.T @ d1 * lr
    # ajusta los pesos de la capa 1

    sesgo_1 -= d1.sum(axis=0, keepdims=True) * lr
    # ajusta el bias de la capa 1

    if (epoca + 1) % 1000 == 0:                        # cada 1000 épocas imprime progreso
        predicciones = np.argmax(a2, axis=1)           # elige la clase con mayor probabilidad
        precision    = np.mean(predicciones == etiquetas) * 100  # % de aciertos
        print(f"  Época {epoca+1:>5}  |  Pérdida: {perdida:.4f}  |  Precisión: {precision:.0f}%")


#  PREDICCIÓN CON FLORES NUEVAS 
nombres = ["Setosa", "Versicolor", "Virginica"]  # nombres legibles de las clases

print("\n✅ Entrenamiento completo!\n")
print("─" * 55)
print("Prueba con flores nuevas (nunca vistas):")
print("─" * 55)

flores_nuevas = np.array([
    [5.1, 3.5, 1.5, 0.3],   # pétalo pequeño → debería ser Setosa
    [6.2, 2.9, 4.3, 1.3],   # pétalo mediano → debería ser Versicolor
    [6.8, 3.0, 5.9, 2.1],   # pétalo grande  → debería ser Virginica
])

flores_norm = (flores_nuevas - datos.min(axis=0)) / (datos.max(axis=0) - datos.min(axis=0))
# normaliza con los MISMOS parámetros del entrenamiento (mismo mínimo y máximo)
# si usáramos parámetros distintos, los números no significarían lo mismo para la red

z1_t = flores_norm @ pesos_1 + sesgo_1  # forward pass capa 1 (sin modificar pesos)
a1_t = relu(z1_t)                       # activación ReLU igual que en entrenamiento
z2_t = a1_t @ pesos_2 + sesgo_2        # forward pass capa 2
probs = softmax(z2_t)                   # probabilidades finales para cada clase

for i, flor in enumerate(flores_nuevas):
    clase     = np.argmax(probs[i])     # índice de la clase con mayor probabilidad
    confianza = probs[i][clase] * 100   # esa probabilidad convertida a porcentaje
    print(f"  Flor {flor}  →  {nombres[clase]}  ({confianza:.1f}% confianza)")

print("─" * 55)