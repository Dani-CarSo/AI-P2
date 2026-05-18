#35
# Q-Learning

import random  # Para decisiones aleatorias (exploración)
import os      # Para limpiar la pantalla en consola
import time    # Para pausar y ver el movimiento


size = 5  # Tamaño del mapa (5x5)

start = (0, 0)  # Posición inicial del agente
goal = (4, 4)   # Posición objetivo (meta)

# Conjunto de celdas que son paredes (no se pueden atravesar)
walls = {
    (1, 1), (1, 2), (2, 2), (3, 1), (3, 3)
}

# Acciones posibles que puede tomar el agente
actions = ["up", "down", "left", "right"]

#  Q-TABLE (MEMORIA DEL AGENTE)

q_table = {}  # Diccionario donde se guardan los valores Q

# Inicializamos cada estado del mapa (excepto paredes)
for x in range(size):
    for y in range(size):
        if (x, y) not in walls:
            # Cada estado tiene valor para cada acción posible
            q_table[(x, y)] = {
                "up": 0,
                "down": 0,
                "left": 0,
                "right": 0
            }


#  PARÁMETROS DE APRENDIZAJE

alpha = 0.1   # Qué tanto aprende en cada actualización
gamma = 0.9   # Importancia del futuro vs presente
epsilon = 0.2 # Probabilidad de explorar (azar)
episodes = 200  # Número de entrenamientos


#  FUNCIÓN DE MOVIMIENTO
def step(state, action):
    x, y = state  # Estado actual del agente

    # Determinar nueva posición según acción
    if action == "up":
        nx, ny = x - 1, y
    elif action == "down":
        nx, ny = x + 1, y
    elif action == "left":
        nx, ny = x, y - 1
    else:
        nx, ny = x, y + 1

    # Si se sale del mapa, no se mueve y recibe penalización
    if nx < 0 or ny < 0 or nx >= size or ny >= size:
        return state, -5, False

    # Si choca con una pared, no se mueve y recibe penalización fuerte
    if (nx, ny) in walls:
        return state, -10, False

    # Si llega a la meta, recibe recompensa positiva y termina episodio
    if (nx, ny) == goal:
        return (nx, ny), 10, True

    # Movimiento normal con pequeña penalización
    return (nx, ny), -1, False


#  POLÍTICA EPSILON-GREEDY
def choose_action(state):
    # A veces explora (elige acción aleatoria)
    if random.random() < epsilon:
        return random.choice(actions)

    # O elige la mejor acción conocida según Q-table
    return max(q_table[state], key=q_table[state].get)


#  MOSTRAR LABERINTO EN CONSOLA

def print_grid(agent_pos):
    # Limpia pantalla (Windows o Linux/Mac)
    os.system("cls" if os.name == "nt" else "clear")

    # Recorre cada celda del mapa
    for x in range(size):
        row = ""
        for y in range(size):

            # Agente
            if (x, y) == agent_pos:
                row += " A "

            # Inicio
            elif (x, y) == start:
                row += " S "

            # Meta
            elif (x, y) == goal:
                row += " G "

            # Pared
            elif (x, y) in walls:
                row += " # "

            # Espacio vacío
            else:
                row += " . "

        print(row)  # Imprime la fila

    print("\n")  # Espacio extra


# ENTRENAMIENTO (Q-LEARNING)

for ep in range(episodes):  # Repite muchos episodios
    state = start  # Reinicia agente

    while state != goal:  # Hasta llegar a la meta

        print_grid(state)  # Muestra el laberinto
        time.sleep(0.2)    # Pausa para ver movimiento

        action = choose_action(state)  # Elige acción
        new_state, reward, done = step(state, action)  # Ejecuta acción

        old_q = q_table[state][action]  # Valor actual Q
        future = max(q_table[new_state].values())  # Mejor futuro

        # Fórmula de Q-Learning
        q_table[state][action] = old_q + alpha * (
            reward + gamma * future - old_q
        )

        state = new_state  # Actualiza estado

        if done:  # Si llegó a la meta
            print_grid(state)
            print("¡Llegó a la meta en el episodio", ep, "!")
            time.sleep(0.5)
            break

print("Entrenamiento terminado ✔")

#  PRUEBA FINAL (SIN EXPLORACIÓN)
input("Presiona ENTER para ver al agente ya entrenado...")

state = start  # Reinicia desde el inicio

while state != goal:  # Hasta llegar a la meta

    print_grid(state)  # Mostrar movimiento
    time.sleep(0.3)    # Pausa visual

    # Siempre elige la mejor acción aprendida
    action = max(q_table[state], key=q_table[state].get)

    state, _, _ = step(state, action)  # Ejecuta movimiento

print_grid(state)
print("¡Meta alcanzada!")