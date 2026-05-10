#73
#Perceptrón, ADALINE y MADALINE


# Importamos random para generar números aleatorios
import random

# ============================================================
# FUNCIÓN DE ACTIVACIÓN
# ============================================================

# Creamos una función llamada activacion
def activacion(valor):

    # Verificamos si el valor es mayor o igual a 0
    if valor >= 0:

        # Si se cumple retornamos 1
        return 1

    # Si no se cumple la condición
    else:

        # Retornamos 0
        return 0


# ============================================================
# PERCEPTRÓN
# ============================================================

# Creamos la función perceptron
def perceptron(x1, x2, w1, w2, bias):

    # Multiplicamos x1 por w1
    parte1 = x1 * w1

    # Multiplicamos x2 por w2
    parte2 = x2 * w2

    # Sumamos todo junto con el bias
    suma = parte1 + parte2 + bias

    # Aplicamos función de activación
    salida = activacion(suma)

    # Retornamos la salida
    return salida


# ============================================================
# ADALINE
# ============================================================

# Creamos función ADALINE
def adaline(x1, x2, w1, w2, bias):

    # Multiplicamos x1 por w1
    parte1 = x1 * w1

    # Multiplicamos x2 por w2
    parte2 = x2 * w2

    # Sumamos resultados y bias
    salida = parte1 + parte2 + bias

    # Retornamos salida lineal
    return salida


# ============================================================
# MADALINE
# ============================================================

# Creamos función MADALINE
def madaline(x1, x2):

    # --------------------------------------------------------
    # PRIMERA NEURONA ADALINE
    # --------------------------------------------------------

    # Generamos peso aleatorio para x1
    w1a = random.uniform(-1, 1)

    # Generamos peso aleatorio para x2
    w2a = random.uniform(-1, 1)

    # Generamos bias aleatorio
    biasa = random.uniform(-1, 1)

    # Ejecutamos primera ADALINE
    salida1 = adaline(x1, x2, w1a, w2a, biasa)

    # --------------------------------------------------------
    # SEGUNDA NEURONA ADALINE
    # --------------------------------------------------------

    # Generamos peso aleatorio para x1
    w1b = random.uniform(-1, 1)

    # Generamos peso aleatorio para x2
    w2b = random.uniform(-1, 1)

    # Generamos bias aleatorio
    biasb = random.uniform(-1, 1)

    # Ejecutamos segunda ADALINE
    salida2 = adaline(x1, x2, w1b, w2b, biasb)

    # --------------------------------------------------------
    # SUMAMOS RESULTADOS
    # --------------------------------------------------------

    # Sumamos ambas salidas
    suma_final = salida1 + salida2

    # Aplicamos función de activación
    resultado = activacion(suma_final)

    # Retornamos resultado final
    return resultado

# Mostramos título
print(" PERCEPTRÓN - ADALINE - MADALINE ")

# Creamos ciclo infinito
while True:

    # --------------------------------------------------------
    # PEDIMOS DATOS AL USUARIO
    # --------------------------------------------------------
    # Pedimos valor para x1
    x1 = float(input("\nIngresa valor de x1: "))

    # Pedimos valor para x2
    x2 = float(input("Ingresa valor de x2: "))

    # --------------------------------------------------------
    # MOSTRAMOS MENÚ
    # --------------------------------------------------------
    # Mostramos opciones disponibles
    print("\nSelecciona algoritmo:")

    # Opción 1
    print("1. Perceptrón")

    # Opción 2
    print("2. ADALINE")

    # Opción 3
    print("3. MADALINE")

    # Opción 4
    print("4. Salir")

    # Guardamos opción elegida
    opcion = input("Opción: ")

    # =======================================================
    # OPCIÓN 1 -> PERCEPTRÓN
    # =======================================================
    # Verificamos si eligió 1
    if opcion == "1":

        # Generamos peso aleatorio para x1
        w1 = random.uniform(-1, 1)

        # Generamos peso aleatorio para x2
        w2 = random.uniform(-1, 1)

        # Generamos bias aleatorio
        bias = random.uniform(-1, 1)

        # Ejecutamos perceptrón
        resultado = perceptron(x1, x2, w1, w2, bias)

        # Mostramos pesos usados
        print("\nPesos usados:")

        # Mostramos w1
        print("w1 =", w1)

        # Mostramos w2
        print("w2 =", w2)

        # Mostramos bias
        print("bias =", bias)

        # Mostramos salida
        print("Salida del Perceptrón:", resultado)

    # ========================================================
    # OPCIÓN 2 -> ADALINE
    # ========================================================
    # Verificamos si eligió 2
    elif opcion == "2":

        # Generamos peso aleatorio para x1
        w1 = random.uniform(-1, 1)

        # Generamos peso aleatorio para x2
        w2 = random.uniform(-1, 1)

        # Generamos bias aleatorio
        bias = random.uniform(-1, 1)

        # Ejecutamos ADALINE
        resultado = adaline(x1, x2, w1, w2, bias)

        # Mostramos pesos usados
        print("\nPesos usados:")

        # Mostramos w1
        print("w1 =", w1)

        # Mostramos w2
        print("w2 =", w2)

        # Mostramos bias
        print("bias =", bias)

        # Mostramos salida
        print("Salida ADALINE:", resultado)

    # ========================================================
    # OPCIÓN 3 -> MADALINE
    # ========================================================
    # Verificamos si eligió 3
    elif opcion == "3":

        # Ejecutamos MADALINE
        resultado = madaline(x1, x2)

        # Mostramos resultado
        print("\nSalida MADALINE:", resultado)

    # ========================================================
    # OPCIÓN 4 -> SALIR
    # ========================================================
    # Verificamos si eligió 4
    elif opcion == "4":

        # Mostramos mensaje final
        print("\nPrograma terminado.")

        # Rompemos el ciclo
        break

    # ========================================================
    # OPCIÓN INCORRECTA
    # ========================================================
    # Si no eligió una opción válida
    else:

        # Mostramos error
        print("\nOpción no válida.")