#33
#Aprendizaje por Refuerzo Pasivo

# Lista de estados (ciudades del sistema)
estados = ["A", "B", "C"]

# Lista donde guardaremos la recompensa inmediata de cada ciudad
recompensas = []

# Mensaje para el usuario
print("\nRecompensa de cada ciudad:")

# Pedimos al usuario la recompensa de cada ciudad
for e in estados:
    # input() recibe un número que representa qué tan buena es la ciudad
    # float() convierte el texto a número decimal
    recompensas.append(float(input(e + ": ")))

# Política fija:
# define a dónde se mueve el agente desde cada estado
# A → B, B → C, C → C (se queda en C)
politica = [1, 2, 2]

# Factor de descuento:
# indica cuánto importa el futuro (0 = no importa, 1 = muy importante)
gamma = float(input("\nGamma (0-1): "))

# Número de iteraciones del algoritmo
# (cuántas veces refinamos los valores)
iteraciones = int(input("Iteraciones: "))

# Inicializamos los valores de cada estado en 0
# V[s] representa el "valor esperado" de cada ciudad
V = [0, 0, 0]

# Bucle principal de aprendizaje (iteración de valores)
for it in range(iteraciones):

    # Copia de los valores actuales (para ir actualizando sin perder los anteriores)
    nuevo = V.copy()

    # Recorremos cada estado
    for s in range(3):

        # Estado al que se transiciona según la política fija
        siguiente = politica[s]

        # ECUACIÓN PRINCIPAL DE RL PASIVO (Bellman):
        # valor del estado = recompensa actual + valor futuro descontado
        nuevo[s] = recompensas[s] + gamma * V[siguiente]

    # Actualizamos los valores con los nuevos calculados
    V = nuevo

    # Mostramos el progreso en cada iteración
    print("\nIteración", it + 1, V)

# Resultado final del algoritmo
print("\n RESULTADO FINAL ")

# Imprimimos el valor de cada ciudad
for i in range(3):
    print(estados[i], "→", round(V[i], 3))