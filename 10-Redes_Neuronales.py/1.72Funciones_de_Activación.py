#72
#Funciones de Activacion

# Importamos la librería math
# Sirve para usar funciones matemáticas como e^x
import math


# ------------------------------------------------------------
# FUNCIÓN ESCALÓN
# ------------------------------------------------------------
# Si el número es mayor o igual a 0 devuelve 1
# Si es menor devuelve 0
def escalon(x):

    # Verificamos si x es mayor o igual a 0
    if x >= 0:

        # Retornamos 1
        return 1

    # Si no se cumple la condición
    else:

        # Retornamos 0
        return 0


# ------------------------------------------------------------
# FUNCIÓN SIGMOIDE
# ------------------------------------------------------------
# Fórmula:
# 1 / (1 + e^-x)
#
# Convierte cualquier número a un valor entre 0 y 1
def sigmoide(x):

    # Aplicamos la fórmula sigmoide
    resultado = 1 / (1 + math.exp(-x))

    # Regresamos el resultado
    return resultado


# ------------------------------------------------------------
# FUNCIÓN TANH
# ------------------------------------------------------------
# Devuelve valores entre -1 y 1
def tanh(x):

    # Usamos la función tanh de math
    resultado = math.tanh(x)

    # Retornamos el resultado
    return resultado


# ------------------------------------------------------------
# FUNCIÓN ReLU
# ------------------------------------------------------------
# Si x es menor que 0 devuelve 0
# Si x es mayor devuelve el mismo valor
def relu(x):

    # Usamos max para elegir el mayor número
    resultado = max(0, x)

    # Regresamos el resultado
    return resultado


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

# Mostramos título
print("===================================")
print(" FUNCIONES DE ACTIVACIÓN")
print("===================================")

# Creamos un ciclo infinito
# para que el usuario pueda seguir probando números
while True:

    # Pedimos un número al usuario
    numero = float(input("\nIngresa un número: "))

    # Mostramos menú de opciones
    print("\nSelecciona una función:")
    print("1. Escalón")
    print("2. Sigmoide")
    print("3. Tanh")
    print("4. ReLU")
    print("5. Salir")

    # Guardamos la opción del usuario
    opcion = input("Opción: ")

    # --------------------------------------------------------
    # OPCIÓN 1 -> ESCALÓN
    # --------------------------------------------------------
    if opcion == "1":

        # Llamamos la función escalón
        resultado = escalon(numero)

        # Mostramos el resultado
        print("Resultado:", resultado)

    # --------------------------------------------------------
    # OPCIÓN 2 -> SIGMOIDE
    # --------------------------------------------------------
    elif opcion == "2":

        # Ejecutamos la función sigmoide
        resultado = sigmoide(numero)

        # Mostramos el resultado
        print("Resultado:", resultado)

    # --------------------------------------------------------
    # OPCIÓN 3 -> TANH
    # --------------------------------------------------------
    elif opcion == "3":

        # Ejecutamos la función tanh
        resultado = tanh(numero)

        # Mostramos el resultado
        print("Resultado:", resultado)

    # --------------------------------------------------------
    # OPCIÓN 4 -> ReLU
    # --------------------------------------------------------
    elif opcion == "4":

        # Ejecutamos la función relu
        resultado = relu(numero)

        # Mostramos el resultado
        print("Resultado:", resultado)

    # OPCIÓN 5 -> SALIR
  
    elif opcion == "5":

        # Mensaje de despedida
        print("Programa finalizado.")

        # Terminamos el ciclo
        break

  
    # SI EL USUARIO ESCRIBE ALGO INCORRECTO
    else:

        # Mostramos mensaje de error
        print("Opción no válida.")