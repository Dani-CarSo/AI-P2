#61
#Algoritmo Hacia Delante-Atrás

# Definimos los estados ocultos del sistema
estados = ["Activo", "Cargando"]

# Pedimos al usuario que ingrese observaciones separadas por coma
entrada = input("Escribe observaciones (Mover,Quieto): ")

# Convertimos el texto en una lista quitando espacios
observaciones = [x.strip() for x in entrada.split(",")]

# Probabilidades iniciales del sistema

inicial = {
    "Activo": 0.8,     # Probabilidad de iniciar activo
    "Cargando": 0.2    # Probabilidad de iniciar cargando
}


# Probabilidades de transición entre estados

transicion = {
    "Activo": {
        "Activo": 0.7,      # Probabilidad de quedarse activo
        "Cargando": 0.3     # Probabilidad de pasar a cargando
    },
    "Cargando": {
        "Activo": 0.4,      # Probabilidad de pasar a activo
        "Cargando": 0.6     # Probabilidad de quedarse cargando
    }
}


# Probabilidades de emisión (observación dada un estado)
emision = {
    "Activo": {
        "Mover": 0.9,       # Si está activo es muy probable que se mueva
        "Quieto": 0.1       # Poco probable que esté quieto
    },
    "Cargando": {
        "Mover": 0.2,       # Poco probable que se mueva cargando
        "Quieto": 0.8       # Más probable que esté quieto
    }
}

# ALGORITMO FORWARD (HACIA DELANTE)
# Lista donde guardamos resultados forward
forward = []

# Diccionario del primer paso
primero = {}

# Calculamos el primer estado con observación inicial
for e in estados:
    # Probabilidad inicial × probabilidad de observación
    primero[e] = inicial[e] * emision[e][observaciones[0]]

# Guardamos el primer paso
forward.append(primero)

# Mostramos resultado inicial
print("\n--- FORWARD ---")
print("Paso 1:", primero)

# Recorremos el resto de observaciones
for t in range(1, len(observaciones)):

    # Diccionario para el estado actual
    actual = {}

    # Recorremos cada posible estado actual
    for e2 in estados:

        # Acumulador de probabilidades
        suma = 0

        # Recorremos estados anteriores
        for e1 in estados:

            # Multiplicamos:
            # forward anterior × transición
            suma += forward[t-1][e1] * transicion[e1][e2]

        # Multiplicamos por la probabilidad de emisión
        actual[e2] = suma * emision[e2][observaciones[t]]

    # Guardamos resultado del paso actual
    forward.append(actual)

    # Mostramos resultado
    print("Paso", t+1, ":", actual)

# ---------------------------------------------------------
# ALGORITMO BACKWARD (HACIA ATRÁS)
# ---------------------------------------------------------

# Lista donde guardamos resultados backward
backward = []

# Caso base: último paso vale 1
final = {
    "Activo": 1,
    "Cargando": 1
}

# Insertamos el último paso al inicio
backward.insert(0, final)

# Mostramos resultado final
print("\n--- BACKWARD ---")
print("Último paso:", final)

# Recorremos desde el penúltimo hasta el primero
for t in range(len(observaciones)-2, -1, -1):

    # Diccionario para estado actual
    actual = {}

    # Recorremos estados actuales
    for e in estados:

        # Acumulador de probabilidades
        suma = 0

        # Recorremos estados siguientes
        for sig in estados:

            # Fórmula backward:
            # transición × emisión × backward siguiente
            suma += (
                transicion[e][sig] *
                emision[sig][observaciones[t+1]] *
                backward[0][sig]
            )

        # Guardamos resultado
        actual[e] = suma

    # Insertamos al inicio de la lista
    backward.insert(0, actual)

    # Mostramos resultado del paso
    print("Paso", t+1, ":", actual)
