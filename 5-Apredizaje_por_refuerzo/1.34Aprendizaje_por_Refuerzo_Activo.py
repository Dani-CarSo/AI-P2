#34
#Aprendizaje por Refuerzo Activo

import random  # Importa la librería random para tomar decisiones aleatorias (exploración)

# DEFINIMOS EL ENTORNO (GRID)

grid = [  # Se crea el mapa del entorno tipo cuadrícula
    ["S", " ", " ", "X"],  # S = inicio, X = obstáculo
    [" ", "X", " ", " "],  # espacios vacíos = caminos libres
    [" ", " ", "X", " "],
    ["X", " ", " ", "G"]   # G = meta
]

# PARÁMETROS DEL APRENDIZAJE
alpha = 0.1   # tasa de aprendizaje (qué tanto se actualiza la Q-table)
gamma = 0.9   # factor de descuento (importancia de recompensas futuras)
epsilon = 0.2 # probabilidad de explorar (no siempre elegir lo mejor)

# ACCIONES POSIBLES DEL AGENTE
actions = ["up", "down", "left", "right"]  # movimientos posibles


# Q-TABLE (memoria del agente)
Q = {}  # diccionario vacío donde se guardan valores Q por estado

# INICIALIZAR ESTADO EN Q-TABLE

def init_state(state):
    if state not in Q:  # si el estado no existe en la tabla
        Q[state] = {a: 0 for a in actions}  # se crean valores 0 para cada acción


# CONVERTIR POSICIÓN A ESTADO

def get_state(pos):
    return str(pos[0]) + "," + str(pos[1])  # convierte (x,y) a string "x,y"

# FUNCIÓN DE MOVIMIENTO

def step(pos, action):
    x, y = pos  # se separa la posición en coordenadas

    if action == "up":  # mover arriba
        x -= 1
    elif action == "down":  # mover abajo
        x += 1
    elif action == "left":  # mover izquierda
        y -= 1
    elif action == "right":  # mover derecha
        y += 1


    # VERIFICAR LÍMITES DEL MAPA

    if x < 0 or x > 3 or y < 0 or y > 3:
        return pos, -5, False  # castigo si se sale del mapa

    cell = grid[x][y]  # revisar qué hay en la nueva posición

    # SI CHOCA CON OBSTÁCULO

    if cell == "X":
        return pos, -5, False  # castigo por choque


    # SI LLEGA A LA META

    if cell == "G":
        return (x, y), 10, True  # recompensa alta y termina episodio

    
    # MOVIMIENTO NORMAL

    return (x, y), -1, False  # pequeño castigo por cada paso


# SELECCIÓN DE ACCIÓN (ε-greedy)

def choose_action(state):
    init_state(state)  # asegurar que el estado exista en Q-table

    if random.random() < epsilon:
        return random.choice(actions)  # exploración aleatoria
    else:
        return max(Q[state], key=Q[state].get)  # explotación (mejor acción)

# ENTRENAMIENTO DEL AGENTE
episodes = 50  # número de intentos de aprendizaje

for ep in range(episodes):  # ciclo de entrenamiento

    pos = (0, 0)  # posición inicial del agente
    state = get_state(pos)  # convertir a estado

    done = False  # bandera de final del episodio

    while not done:  # mientras no llegue a la meta

        action = choose_action(state)  # elegir acción

        new_pos, reward, done = step(pos, action)  # ejecutar acción

        new_state = get_state(new_pos)  # nuevo estado

        init_state(new_state)  # asegurarse que existe en Q-table

    
        # ACTUALIZACIÓN Q-LEARNING

        Q[state][action] = Q[state][action] + alpha * (
            reward + gamma * max(Q[new_state].values()) - Q[state][action]
        )

        pos = new_pos  # actualizar posición
        state = new_state  # actualizar estado

    print("Episodio", ep + 1, "terminado")  # mostrar progreso

# MODO INTERACTIVO (USUARIO JUEGA)

print("\n=== MODO INTERACTIVO ===")
print("Controles: w=arriba, s=abajo, a=izquierda, d=derecha")

pos = (0, 0)  # reinicia posición

while True:  # juego infinito hasta llegar a meta

    print("\nPosición:", pos)  # mostrar posición actual

    move = input("Movimiento: ")  # leer movimiento del usuario

    if move == "w":
        action = "up"
    elif move == "s":
        action = "down"
    elif move == "a":
        action = "left"
    elif move == "d":
        action = "right"
    else:
        print("Movimiento inválido")
        continue  # volver a pedir input

    pos, reward, done = step(pos, action)  # ejecutar movimiento

    print("Recompensa:", reward)  # mostrar recompensa obtenida

    if done:  # si llegó a la meta
        print("¡Llegaste a la meta!")
        break  # termina el juego