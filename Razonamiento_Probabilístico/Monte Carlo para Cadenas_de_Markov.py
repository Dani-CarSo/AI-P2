#57
#Monte Carlo para Cadenas de Markov

# Importamos random para generar movimientos aleatorios
import random

# Mostramos el título del programa
print("=== Cadenas de Markov con Monte Carlo ===")


# ESTADOS POSIBLES
# Cada estado representa una habitación

habitaciones = ["Sala", "Cocina", "Recamara"]


# TRANSICIONES DE MARKOV
# Cada habitación tiene probabilidades
# de ir a otra habitación

transiciones = {

    # Desde Sala
    "Sala": {
        "Sala": 0.2,
        "Cocina": 0.5,
        "Recamara": 0.3
    },

    # Desde Cocina
    "Cocina": {
        "Sala": 0.6,
        "Cocina": 0.1,
        "Recamara": 0.3
    },

    # Desde Recamara
    "Recamara": {
        "Sala": 0.4,
        "Cocina": 0.2,
        "Recamara": 0.4
    }
}

# ESTADO INICIAL
# Comenzamos en la Sala

estado_actual = "Sala"

# Mostramos el estado inicial
print("\nInicio en:", estado_actual)

# SIMULACIÓN MONTE CARLO
# Repetimos movimientos aleatorios
# usando las probabilidades

for paso in range(10):

    # Obtenemos las opciones posibles
    opciones = list(transiciones[estado_actual].keys())

    # Obtenemos las probabilidades
    probabilidades = list(transiciones[estado_actual].values())

    # Elegimos el siguiente estado
    siguiente_estado = random.choices(
        opciones,
        probabilidades
    )[0]

    # Mostramos el movimiento
    print("Paso", paso + 1, "->", siguiente_estado)

    # Actualizamos el estado actual
    estado_actual = siguiente_estado