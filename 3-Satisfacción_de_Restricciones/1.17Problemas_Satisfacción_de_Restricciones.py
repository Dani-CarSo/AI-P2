#17
#Problemas de Satisfacción de Restricciones

def es_valido(tablero, fila, col, num):  # Define la función que valida si un número puede ir en una celda
    if num in tablero[fila]:             # Revisa si 'num' ya existe en la fila actual
        return False                     # Si ya está en la fila, no es válido → retorna False

    for i in range(9):                   # Recorre las 9 filas de la columna 'col'
        if tablero[i][col] == num:       # Revisa si 'num' ya existe en esa columna
            return False                 # Si ya está en la columna, no es válido → retorna False

    inicio_fila = fila - fila % 3       # Calcula la fila inicial del subcuadro 3×3 (0, 3 o 6)
    inicio_col = col - col % 3          # Calcula la columna inicial del subcuadro 3×3 (0, 3 o 6)

    for i in range(3):                   # Recorre las 3 filas del subcuadro
        for j in range(3):               # Recorre las 3 columnas del subcuadro
            if tablero[inicio_fila + i][inicio_col + j] == num:  # Revisa si 'num' ya está en el subcuadro
                return False             # Si ya está en el subcuadro, no es válido → retorna False

    return True                          # Si pasó todas las validaciones, el número sí puede ir ahí


def resolver_sudoku(tablero):            # Define la función principal que resuelve el Sudoku
    for fila in range(9):                # Recorre cada una de las 9 filas del tablero
        for col in range(9):             # Recorre cada una de las 9 columnas del tablero
            if tablero[fila][col] == 0:  # Si la celda está vacía (valor 0)
                for num in range(1, 10): # Prueba colocar cada número del 1 al 9
                    if es_valido(tablero, fila, col, num):  # Si el número es válido en esa posición
                        tablero[fila][col] = num             # Lo coloca temporalmente en la celda
                        if resolver_sudoku(tablero):         # Llama recursivamente para resolver el resto
                            return True                      # Si el resto se resolvió, retorna True
                        tablero[fila][col] = 0               # Si falló, deshace el número (backtrack)
                return False             # Ningún número funcionó en esta celda → retorna False al nivel anterior
    return True                          # No quedan celdas vacías → el Sudoku está completamente resuelto


def imprimir_tablero(tablero):                              # Define la función para mostrar el tablero
    for fila in tablero:                                    # Recorre cada fila del tablero
        print(" ".join(str(num) for num in fila))           # Imprime los números de la fila separados por espacios


tablero = [                              # Define el tablero inicial del Sudoku
    [5,3,0,0,7,0,0,0,0],                # Fila 0: ceros representan celdas vacías
    [6,0,0,1,9,5,0,0,0],                # Fila 1
    [0,9,8,0,0,0,0,6,0],                # Fila 2
    [8,0,0,0,6,0,0,0,3],                # Fila 3
    [4,0,0,8,0,3,0,0,1],                # Fila 4
    [7,0,0,0,2,0,0,0,6],                # Fila 5
    [0,6,0,0,0,0,2,8,0],                # Fila 6
    [0,0,0,4,1,9,0,0,5],                # Fila 7
    [0,0,0,0,8,0,0,7,9]                 # Fila 8
]

if resolver_sudoku(tablero):             # Ejecuta el solver; si retorna True, encontró solución
    print("Solución encontrada:\n")      # Imprime encabezado de éxito
    imprimir_tablero(tablero)            # Muestra el tablero resuelto
else:                                    # Si retornó False, no hay solución posible
    print("No tiene solución")           # Informa que el Sudoku no tiene solución