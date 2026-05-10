#55
#Muestreo Directo y por rechazo


import random

# Aquí elegimos un clima usando
# probabilidades definidas.

print("=== MUESTREO DIRECTO ===")

# Lista de posibles climas
climas = ["Soleado", "Nublado", "Lluvioso"]

# Probabilidades de cada clima
# Soleado = 50%
# Nublado = 30%
# Lluvioso = 20%
probabilidades = [0.5, 0.3, 0.2]

# random.choices elige según las probabilidades
resultado_directo = random.choices(climas, probabilidades)[0]

# Mostramos el resultado
print("Clima generado:", resultado_directo)

# Generamos números aleatorios
# y aceptamos solo algunos.

print("\nMUESTREO POR RECHAZO ")

while True:

    # Número aleatorio entre 0 y 1
    x = random.random()

    # Otro número aleatorio para decidir
    y = random.random()

    # Función de aceptación
    # Mientras más pequeño sea x,
    # más fácil será aceptado
    if y < (1 - x):

        # Si se acepta, terminamos
        print("Número aceptado:", round(x, 3))
        break

    else:
        # Si no se acepta, se rechaza
        print("Número rechazado:", round(x, 3))