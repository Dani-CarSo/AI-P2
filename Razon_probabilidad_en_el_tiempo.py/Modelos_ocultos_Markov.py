#62
#Modelos Ocultos de Markov

# Definimos los estados ocultos del sistema
estados = ["Cansado", "Energico"]

# Pedimos al usuario las observaciones separadas por coma
entrada = input("Escribe observaciones (Lento,Rapido): ")

# Convertimos la entrada en una lista eliminando espacios
observaciones = [x.strip() for x in entrada.split(",")]

# ---------------------------------------------------------
# PROBABILIDADES INICIALES
# ---------------------------------------------------------

# Probabilidad de iniciar en cada estado
inicial = {
    "Cansado": 0.6,     # 60% de iniciar cansado
    "Energico": 0.4     # 40% de iniciar enérgico
}

# ---------------------------------------------------------
# MATRIZ DE TRANSICIÓN
# ---------------------------------------------------------

# Probabilidad de cambiar entre estados
transicion = {
    "Cansado": {
        "Cansado": 0.7,      # se mantiene cansado
        "Energico": 0.3      # se vuelve enérgico
    },
    "Energico": {
        "Cansado": 0.4,      # se cansa
        "Energico": 0.6      # se mantiene enérgico
    }
}

# ---------------------------------------------------------
# MATRIZ DE EMISIÓN
# ---------------------------------------------------------
# Probabilidad de observar algo dado el estado oculto
emision = {
    "Cansado": {
        "Lento": 0.8,        # si está cansado se mueve lento
        "Rapido": 0.2        # raro que esté rápido
    },
    "Energico": {
        "Lento": 0.3,        # a veces lento
        "Rapido": 0.7        # normalmente rápido
    }
}


# ALGORITMO FORWARD (HACIA DELANTE)
# Lista donde guardamos resultados
forward = []

# Diccionario del primer paso
primero = {}

# Recorremos cada estado
for e in estados:

    # Probabilidad inicial × observación
    primero[e] = inicial[e] * emision[e][observaciones[0]]

# Guardamos el primer resultado
forward.append(primero)

# Mostramos resultado
print("\n--- FORWARD ---")
print("Paso 1:", primero)

# Recorremos el resto de observaciones
for t in range(1, len(observaciones)):

    # Diccionario del paso actual
    actual = {}

    # Recorremos estados posibles
    for e2 in estados:

        # acumulador de probabilidades
        suma = 0

        # recorremos estados anteriores
        for e1 in estados:

            # forward anterior × transición
            suma += forward[t-1][e1] * transicion[e1][e2]

        # multiplicamos por emisión
        actual[e2] = suma * emision[e2][observaciones[t]]

    # guardamos resultado
    forward.append(actual)

    # mostramos resultado
    print("Paso", t+1, ":", actual)

# ---------------------------------------------------------
# ALGORITMO BACKWARD (HACIA ATRÁS)
# ---------------------------------------------------------

# Lista para backward
backward = []

# Caso base: al final todo vale 1
ultimo = {
    "Cansado": 1,
    "Energico": 1
}

# Insertamos el último paso
backward.insert(0, ultimo)

# Mostramos resultado final
print("\n--- BACKWARD ---")
print("Último paso:", ultimo)

# Recorremos hacia atrás
for t in range(len(observaciones)-2, -1, -1):

    # Diccionario actual
    actual = {}

    # Recorremos estados
    for e in estados:

        # acumulador
        suma = 0

        # recorremos siguientes estados
        for sig in estados:

            # backward = transición × emisión × backward siguiente
            suma += (
                transicion[e][sig] *
                emision[sig][observaciones[t+1]] *
                backward[0][sig]
            )

        # guardamos resultado
        actual[e] = suma

    # insertamos al inicio
    backward.insert(0, actual)

    # mostramos resultado
    print("Paso", t+1, ":", actual)

