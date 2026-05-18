#74
# REDES MULTICAPA 

# Esta librería sirve para generar números aleatorios
import random

# Se usa para funciones matemáticas
import math

# Creamos función llamada sigmoide
def sigmoide(x):

    # Aplicamos fórmula sigmoide
    resultado = 1 / (1 + math.exp(-x))

    # Retornamos resultado
    return resultado

# Creamos función neurona_oculta
def neurona_oculta(x1, x2, w1, w2, bias):

    # Multiplicamos x1 por w1
    parte1 = x1 * w1

    # Multiplicamos x2 por w2
    parte2 = x2 * w2

    # Sumamos todo con el bias
    suma = parte1 + parte2 + bias

    # Aplicamos función sigmoide
    salida = sigmoide(suma)

    # Retornamos salida
    return salida


# Creamos función red_multicapa
def red_multicapa(x1, x2):

    # Generamos pesos aleatorios para neurona 1
    w1 = random.uniform(-1, 1)
    w2 = random.uniform(-1, 1)

    # Generamos bias aleatorio
    bias1 = random.uniform(-1, 1)

    # Ejecutamos primera neurona oculta
    salida_oculta1 = neurona_oculta(x1, x2, w1, w2, bias1)

    # Generamos pesos aleatorios para neurona 2
    w3 = random.uniform(-1, 1)
    w4 = random.uniform(-1, 1)

    # Generamos bias aleatorio
    bias2 = random.uniform(-1, 1)

    # Ejecutamos segunda neurona oculta
    salida_oculta2 = neurona_oculta(x1, x2, w3, w4, bias2)

    # Generamos pesos para salida
    ws1 = random.uniform(-1, 1)
    ws2 = random.uniform(-1, 1)

    # Generamos bias final
    bias_salida = random.uniform(-1, 1)

    # Calculamos suma final
    suma_final = (
        salida_oculta1 * ws1
        + salida_oculta2 * ws2
        + bias_salida
    )

    # Aplicamos sigmoide final
    salida_final = sigmoide(suma_final)

    # Retornamos resultado final
    return salida_final

# Mostramos nombre
print(" REDES MULTICAPA ")

# Creamos ciclo infinito
while True:

    # --------------------------------------------------------
    # PEDIMOS DATOS AL USUARIO
    # --------------------------------------------------------

    # Pedimos valor de x1
    x1 = float(input("\nIngresa valor de x1: "))

    # Pedimos valor de x2
    x2 = float(input("Ingresa valor de x2: "))

    # --------------------------------------------------------
    # EJECUTAMOS RED MULTICAPA
    # --------------------------------------------------------

    # Guardamos resultado
    resultado = red_multicapa(x1, x2)

    # --------------------------------------------------------
    # MOSTRAMOS RESULTADO
    # --------------------------------------------------------

    # Mostramos salida final
    print("\nSalida de la Red Multicapa:", resultado)

    # --------------------------------------------------------
    # EXPLICACIÓN
    # --------------------------------------------------------

    # Si resultado es mayor o igual a 0.5
    if resultado >= 0.5:

        # Mostramos mensaje
        print("La red activó una salida positiva.")

    # Si no
    else:

        # Mostramos mensaje
        print("La red activó una salida negativa.")

    # --------------------------------------------------------
    # PREGUNTAMOS SI QUIERE CONTINUAR
    # --------------------------------------------------------

    # Guardamos respuesta
    continuar = input("\n¿Quieres probar otra vez? (si/no): ")

    # Verificamos si quiere salir
    if continuar.lower() == "no":

        # Mostramos mensaje final
        print("\nPrograma terminado.")

        # Terminamos ciclo
        break