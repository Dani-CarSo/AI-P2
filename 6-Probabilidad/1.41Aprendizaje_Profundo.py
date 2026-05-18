#41
#Aprendizaje Profundo


# Importamos TensorFlow
# TensorFlow sirve para crear inteligencia artificial
import tensorflow as tf

# Importamos el dataset MNIST
# MNIST contiene miles de imágenes de números escritos
from tensorflow.keras.datasets import mnist


# CARGAR DATOS
# Cargamos datos de entrenamiento y prueba
# x_train = imágenes para entrenar
# y_train = respuestas correctas
# x_test = imágenes para probar
# y_test = respuestas correctas de prueba
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# NORMALIZAR IMAGENES
# Dividimos entre 255
# Así convertimos los pixeles de 0-255 a 0-1
# Esto ayuda a que la IA aprenda mejor
x_train = x_train / 255.0

# También normalizamos imágenes de prueba
x_test = x_test / 255.0

# CREAR RED NEURONAL

# Creamos un modelo secuencial
# Las capas se ejecutan una después de otra
modelo = tf.keras.models.Sequential([

    # Flatten convierte la imagen 28x28
    # en una sola lista de números
    tf.keras.layers.Flatten(input_shape=(28, 28)),

    # Primera capa oculta
    # Tiene 128 neuronas
    # relu ayuda a aprender patrones
    tf.keras.layers.Dense(
        128,
        activation='relu'
    ),

    # Segunda capa oculta
    # Tiene 64 neuronas
    tf.keras.layers.Dense(
        64,
        activation='relu'
    ),

    # Capa de salida
    # Tiene 10 neuronas porque hay números del 0 al 9
    tf.keras.layers.Dense(
        10,
        activation='softmax'
    )
])


# Compilamos el modelo
modelo.compile(

    # Adam = algoritmo que ajusta el aprendizaje
    optimizer='adam',

    # Función de error para clasificación múltiple
    loss='sparse_categorical_crossentropy',

    # Mostrar precisión del modelo
    metrics=['accuracy']
)


# ENTRENAR IA
# Mostrar mensaje
print("Entrenando inteligencia artificial...\n")

# Entrenamos la red neuronal
modelo.fit(

    # Imágenes de entrenamiento
    x_train,

    # Respuestas correctas
    y_train,

    # Veces que la IA estudiará los datos
    epochs=3,

    # Mostrar progreso del entrenamiento
    verbose=1
)

# Mensaje cuando termina
print("\nEntrenamiento terminado.")

# Ciclo infinito
while True:

    # Mostrar menú
    print("\n========== MENU ==========")

    # Explicar rango válido
    print("Escribe un número del 0 al 9999")

    # Explicar qué hace la IA
    print("La IA intentará reconocer la imagen")

    # Explicar cómo salir
    print("Escribe -1 para salir")

    # Pedimos un número al usuario
    indice = int(input("\n¿Qué imagen quieres probar?: "))


    # SALIR DEL PROGRAMA
    # Si el usuario escribe -1
    if indice == -1:

        # Mostrar mensaje
        print("\nPrograma terminado.")

        # Romper ciclo
        break


    # VALIDAR NUMERO
    # Revisar si el número está fuera de rango
    if indice < 0 or indice >= 10000:

        # Mostrar error
        print("Número fuera de rango.")

        # Regresar al menú
        continue


    # La IA analiza la imagen
    prediccion = modelo.predict(

        # reshape convierte la imagen
        # al formato que necesita TensorFlow
        x_test[indice].reshape(1, 28, 28),

        # No mostrar mensajes extra
        verbose=0
    )

    # Buscar la neurona con mayor probabilidad
    resultado = prediccion.argmax()


    print("\nRESULTADOS ")

    # Mostrar número verdadero
    print("Número real:", y_test[indice])

    # Mostrar número que creyó la IA
    print("La IA cree que es:", resultado)

    # Obtener porcentaje de confianza
    confianza = prediccion[0][resultado] * 100

    # Mostrar confianza
    print(
        "Confianza:",
        round(confianza, 2),
        "%"
    )