#75
#Separabilidad Lineal

import random

# Creamos función llamada separabilidad_lineal
def separabilidad_lineal(x1, x2, w1, w2, bias):

    # Multiplicamos x1 por w1
    parte1 = x1 * w1

    # Multiplicamos x2 por w2
    parte2 = x2 * w2

    # Sumamos resultados y bias
    resultado = parte1 + parte2 + bias

    # Retornamos resultado
    return resultado



# Mostramos título
print(" SEPARABILIDAD LINEAL ")

# GENERAMOS PESOS ALEATORIOS
# Generamos peso aleatorio para x1
w1 = random.uniform(-2, 2)

# Generamos peso aleatorio para x2
w2 = random.uniform(-2, 2)

# Generamos bias aleatorio
bias = random.uniform(-2, 2)

# MOSTRAMOS PESOS GENERADOS
# Mostramos mensaje
print("\nPesos generados:")

# Mostramos valor de w1
print("w1 =", w1)

# Mostramos valor de w2
print("w2 =", w2)

# Mostramos valor de bias
print("bias =", bias)

# MOSTRAMOS ECUACIÓN
# Mostramos mensaje
print("\nEcuación utilizada:")

# CICLO PRINCIPAL
# Creamos ciclo infinito
while True:

    # PEDIMOS DATOS AL USUARIO
    # Pedimos valor para x1
    x1 = float(input("\nIngresa valor de x1: "))

    # Pedimos valor para x2
    x2 = float(input("Ingresa valor de x2: "))

    # EJECUTAMOS ALGORITMO
    # Guardamos resultado
    resultado = separabilidad_lineal(x1, x2, w1, w2, bias)

    # MOSTRAMOS RESULTADO
    # Mostramos resultado matemático
    print("\nResultado:", resultado)

    # ANALIZAMOS POSICIÓN DEL PUNTO
    # Verificamos si el resultado es positivo
    if resultado >= 0:

        # Mostramos mensaje
        print("El punto quedó de un lado de la línea.")

    # Si el resultado es negativo
    else:

        # Mostramos mensaje
        print("El punto quedó del otro lado de la línea.")

    # PREGUNTAMOS SI QUIERE CONTINUAR
    # Guardamos respuesta
    continuar = input("\n¿Quieres probar otro punto? (si/no): ")

    # VERIFICAMOS SI QUIERE SALIR
    # Convertimos texto a minúsculas
    if continuar.lower() == "no":

        # Mostramos mensaje final
        print("\nPrograma terminado.")

        # Terminamos ciclo
        break