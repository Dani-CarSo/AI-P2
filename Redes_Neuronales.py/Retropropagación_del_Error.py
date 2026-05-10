#76
# RETROPROPAGACIÓN DEL ERROR

import random
import math


# FUNCIÓN SIGMOIDE
# Creamos función sigmoide
def sigmoide(x):

    # Aplicamos fórmula sigmoide
    return 1 / (1 + math.exp(-x))


# DERIVADA DE LA SIGMOIDE
# Creamos función derivada
def derivada(y):

    # Calculamos derivada
    return y * (1 - y)


# INICIALIZAMOS PESOS
# Generamos peso aleatorio para x1
w1 = random.uniform(-1, 1)

# Generamos peso aleatorio para x2
w2 = random.uniform(-1, 1)

# Generamos bias aleatorio
bias = random.uniform(-1, 1)


# DEFINIMOS TASA DE APRENDIZAJE
# Valor de aprendizaje
learning_rate = 0.5

# Mostramos título
print(" BACKPROPAGATION ")


# Mostramos ecuación principal
print("\nLa neurona utiliza:")



# CICLO PRINCIPAL
# Creamos ciclo infinito
while True:

    # PEDIMOS DATOS
    # Pedimos entrada x1
    x1 = float(input("\nIngresa x1: "))

    # Pedimos entrada x2
    x2 = float(input("Ingresa x2: "))

    # Pedimos salida deseada
    objetivo = float(input("Ingresa resultado esperado (0 o 1): "))


    # PROPAGACIÓN HACIA ADELANTE
    # Calculamos suma ponderada
    suma = (x1 * w1) + (x2 * w2) + bias

    # Aplicamos sigmoide
    salida = sigmoide(suma)



    # Calculamos diferencia entre objetivo y salida
    error = objetivo - salida



    # Calculamos delta
    delta = error * derivada(salida)


    # Ajustamos w1
    w1 += learning_rate * delta * x1

    # Ajustamos w2
    w2 += learning_rate * delta * x2

    # Ajustamos bias
    bias += learning_rate * delta


    # Mostramos salida actual
    print("\nSalida generada:", salida)

    # Mostramos error actual
    print("Error:", error)

    # Mostramos pesos nuevos
    print("\nNuevos pesos:")

    # Mostramos w1
    print("w1 =", w1)

    # Mostramos w2
    print("w2 =", w2)

    # Mostramos bias
    print("bias =", bias)


    # Si el error es pequeño
    if abs(error) < 0.2:

        # Mostramos mensaje
        print("La red neuronal aprendió bastante bien.")

    # Si el error sigue siendo grande
    else:

        # Mostramos mensaje
        print("La red aún sigue ajustando pesos.")



    # Guardamos respuesta
    continuar = input("\n¿Quieres hacer otra prueba? (si/no): ")


    # Verificamos respuesta
    if continuar.lower() == "no":

        # Mostramos mensaje final
        print("\nPrograma terminado.")

        # Rompemos ciclo
        break