#59
#Procesos de Markov

# Importamos random para usar probabilidades
import random

# Estado inicial de la máquina
estado = "Esperando moneda"

# Cantidad de pasos de la simulación
pasos = 12

# Título
print("Simulación de una máquina usando Procesos de Markov\n")

# Repetimos la simulación
for i in range(1, pasos + 1):

    # Mostramos el estado actual
    print("Paso", i, "->", estado)

    # El siguiente estado depende SOLO del estado actual
    # Si la máquina espera moneda
    if estado == "Esperando moneda":

        # Número aleatorio
        numero = random.random()

        # 80% de probabilidad de insertar moneda
        if numero < 0.8:
            estado = "Seleccionando producto"

        # 20% de seguir esperando
        else:
            estado = "Esperando moneda"

    # Si el usuario selecciona producto
    elif estado == "Seleccionando producto":

        # Número aleatorio
        numero = random.random()

        # 90% de entregar producto
        if numero < 0.9:
            estado = "Entregando producto"

        # 10% de cancelar
        else:
            estado = "Esperando moneda"

    # Si la máquina entrega el producto
    elif estado == "Entregando producto":

        # Después de entregar vuelve al inicio
        estado = "Esperando moneda"

