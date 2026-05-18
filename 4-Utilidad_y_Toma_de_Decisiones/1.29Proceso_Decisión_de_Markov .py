#29
#Proceso de Decisión de Markov (MDP)

# Laberinto interactivo
# Este programa permite mover un jugador dentro de un mapa hasta llegar a la meta
laberinto = [
    ["S", ".", "."],   # Fila 0 "S" es inicio, "." son espacios libres
    [".", "X", "."],   # Fila 1 "X" es un obstáculo
    [".", ".", "G"]    # Fila 2 "G" es la meta 
]

# posición inicial
pos = [0, 0]  
# El jugador empieza en la fila 0, columna 0 (donde está "S")

def mostrar():
    # Función para imprimir el laberinto en pantalla
    for i in range(len(laberinto)):
        # Recorre cada fila del laberinto (i = índice de fila)
        fila = ""
        # Variable donde se va a construir el texto de la fila
        for j in range(len(laberinto[0])):
            # Recorre cada columna (j = índice de columna)
            if [i, j] == pos:
                # Si la posición actual coincide con la del jugador
                fila += "P "  
                # Se imprime "P" para representar al jugador
            else:
                # Si no es la posición del jugador
                fila += laberinto[i][j] + " "
                # Se imprime lo que hay en el mapa (., X o G)
        print(fila)
        # Imprime la fila completa del laberinto
    print()
    # Salto de línea para que se vea más limpio

print(" Llega a la meta (G). Evita X.\n")
# Mensaje inicial para el jugador

while True:
    # Bucle infinito → el juego sigue hasta que ganes
    mostrar()
    # Muestra el estado actual del laberinto
    move = input("Mover (w/a/s/d): ")
    # Pide al usuario una acción:
    # w = arriba, s = abajo, a = izquierda, d = derecha
    nueva_pos = pos.copy()
    # Se hace una copia de la posición actual para calcular el movimiento
    # (así no modificamos la original hasta validar)
    if move == "w":
        # Si presiona "w" (arriba)
        nueva_pos[0] -= 1
        # Disminuye la fila → se mueve hacia arriba
    elif move == "s":
        # Si presiona "s" (abajo)
        nueva_pos[0] += 1
        # Aumenta la fila → se mueve hacia abajo
    elif move == "a":
        # Si presiona "a" (izquierda)
        nueva_pos[1] -= 1
        # Disminuye la columna → se mueve a la izquierda
    elif move == "d":
        # Si presiona "d" (derecha)
        nueva_pos[1] += 1
        # Aumenta la columna → se mueve a la derecha
        
    else:
        # Si el usuario escribe algo distinto
        print("Movimiento inválido")
        # Muestra error
        continue
        # Regresa al inicio del bucle sin hacer más

    # verificar límites
    if (0 <= nueva_pos[0] < len(laberinto) and
        0 <= nueva_pos[1] < len(laberinto[0])):
        # Verifica que la nueva posición esté dentro del mapa
        # (no salirte por arriba, abajo, izquierda o derecha)

        if laberinto[nueva_pos[0]][nueva_pos[1]] == "X":
            # Si la nueva posición es un obstáculo
            
            print("Haz chocado, intenta de nuevo!")
            # Muestra mensaje de choque (NO te mueves)
        else:
            # Si no hay obstáculo
            
            pos = nueva_pos
            # Se actualiza la posición → el jugador se mueve

    # ganar
    if laberinto[pos[0]][pos[1]] == "G":
        # Verifica si la posición actual es la meta
        
        print(" ¡Llegaste a la meta!")
        # Mensaje de victoria
        
        break
        # Termina el juego (sale del while)