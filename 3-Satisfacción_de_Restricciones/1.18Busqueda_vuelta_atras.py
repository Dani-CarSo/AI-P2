#18
# Búsqueda de Vuelta Atrás

def es_seguro(tablero, fila, col, n):    # Define la función que verifica si una reina puede colocarse en (fila, col)

    for i in range(fila):                # Recorre todas las filas anteriores a la actual
        if tablero[i][col] == 1:         # Revisa si ya hay una reina en la misma columna
            return False                 # Si hay una reina arriba, la posición no es segura → retorna False

    i, j = fila - 1, col - 1            # Inicializa i y j en la celda diagonal superior-izquierda
    while i >= 0 and j >= 0:            # Recorre mientras no salga del tablero por arriba o por la izquierda
        if tablero[i][j] == 1:          # Revisa si hay una reina en esa diagonal
            return False                 # Si hay una reina en la diagonal izquierda → retorna False
        i -= 1                           # Sube una fila
        j -= 1                           # Se mueve una columna a la izquierda

    i, j = fila - 1, col + 1            # Inicializa i y j en la celda diagonal superior-derecha
    while i >= 0 and j < n:             # Recorre mientras no salga del tablero por arriba o por la derecha
        if tablero[i][j] == 1:          # Revisa si hay una reina en esa diagonal
            return False                 # Si hay una reina en la diagonal derecha → retorna False
        i -= 1                           # Sube una fila
        j += 1                           # Se mueve una columna a la derecha

    return True                          # Pasó todas las verificaciones → la posición es segura


def resolver_n_reinas(tablero, fila, n): # Define la función de backtracking que resuelve el problema
    if fila == n:                        # Caso base: si ya se colocaron reinas en las n filas, está resuelto
        return True                      # Retorna True indicando que se encontró una solución válida

    for col in range(n):                 # Prueba colocar una reina en cada columna de la fila actual
        if es_seguro(tablero, fila, col, n):   # Verifica si la posición (fila, col) es segura
            tablero[fila][col] = 1             # Coloca la reina temporalmente en esa posición
            if resolver_n_reinas(tablero, fila + 1, n):  # Llama recursivamente para colocar la reina en la siguiente fila
                return True                    # Si la recursión resolvió el resto, retorna True
            tablero[fila][col] = 0             # Si falló, quita la reina (backtrack) y prueba la siguiente columna

    return False                         # Ninguna columna funcionó en esta fila → retorna False al nivel anterior


n = 4                                    # Define el tamaño del tablero (4×4) y el número de reinas a colocar

tablero = [[0 for _ in range(n)] for _ in range(n)]  # Crea un tablero n×n inicializado con ceros (celdas vacías)

if resolver_n_reinas(tablero, 0, n):     # Ejecuta el solver desde la fila 0; si retorna True, encontró solución
    print("Solución encontrada:\n")      # Imprime encabezado de éxito
    for fila in tablero:                 # Recorre cada fila del tablero resuelto
        print(fila)                      # Imprime la fila (1 = reina colocada, 0 = celda vacía)
else:                                    # Si retornó False, no existe ninguna solución posible
    print("No hay solución")             # Informa que el problema no tiene solución para este n