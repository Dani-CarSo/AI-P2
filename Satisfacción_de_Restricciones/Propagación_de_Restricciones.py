#19
#Propagación de Restricciones

# deque es una cola de doble extremo (más eficiente que list para popleft)
from collections import deque
# copy permite hacer copias profundas de estructuras anidadas (listas de sets)
import copy

# ─── Utilidades de índices ───────────────────────────────────────────────────

def idx(r, c):
    # Convierte coordenadas (fila, columna) a un índice lineal 0..80
    # Ejemplo: (0,0)=0, (0,8)=8, (1,0)=9, (8,8)=80
    return r * 9 + c

def rc(i):
    # Operación inversa: dado un índice lineal, devuelve (fila, columna)
    # Ejemplo: 10 → (1, 1) porque 10//9=1 y 10%9=1
    return i // 9, i % 9

def peers(r, c):
    # Calcula todos los índices que comparten restricción con la celda (r,c)
    # En Sudoku una celda NO puede repetir valor con ninguna de sus "peers"

    # Todas las celdas de la misma fila r (columnas 0..8)
    fila = {idx(r, j) for j in range(9)}

    # Todas las celdas de la misma columna c (filas 0..8)
    col  = {idx(i, c) for i in range(9)}

    # Esquina superior izquierda de la caja 3x3 a la que pertenece (r,c)
    # Ejemplo: (4,5) → br=3, bc=3 (caja central)
    br, bc = (r // 3) * 3, (c // 3) * 3

    # Todas las celdas dentro de esa caja 3x3
    caja = {idx(br + i, bc + j) for i in range(3) for j in range(3)}

    # Unión de las tres zonas, quitando la celda misma (no es peer de sí misma)
    return (fila | col | caja) - {idx(r, c)}

def todos_los_arcos():
    # Un "arco" (xi, xj) representa la restricción xi ≠ xj
    # Necesitamos todos los pares de celdas que se restringen mutuamente
    arcos = []
    for r in range(9):             # recorre las 9 filas
        for c in range(9):         # recorre las 9 columnas
            xi = idx(r, c)         # índice de la celda actual
            for xj in peers(r, c): # para cada vecino restringido
                arcos.append((xi, xj))  # agrega el arco dirigido xi→xj
    return arcos                   # devuelve lista con todos los arcos


# ─── AC-3 ────────────────────────────────────────────────────────────────────

def revisar(dominios, xi, xj):
    # Intenta reducir el dominio de xi eliminando valores sin soporte en xj
    # "soporte" significa: existe al menos un valor en xj con el que xi es compatible
    # Para Sudoku la restricción es xi ≠ xj, así que val en xi tiene soporte
    # si y solo si xj contiene algún valor distinto de val

    revisado = False               # bandera: indica si se eliminó algo

    for val in list(dominios[xi]): # itera sobre copia del dominio (no modificar mientras iteras)

        # Busca si existe algún v en xj tal que v != val (soporte para val)
        # Si NO existe ninguno → val no tiene soporte → se elimina
        if not any(v != val for v in dominios[xj]):
            dominios[xi].discard(val)  # elimina val del dominio de xi
            revisado = True            # marca que hubo cambio

    return revisado  # True si el dominio se redujo, False si no cambió nada


def ac3(dominios, arcos=None, verbose=True):
    # Implementación del algoritmo AC-3 (Arc Consistency 3)
    # Procesa arcos uno a uno; si un dominio cambia, reagrega los arcos afectados

    # Inicializa la cola con los arcos dados, o con TODOS los arcos del Sudoku
    queue = deque(arcos or todos_los_arcos())

    podas = 0  # contador de veces que un dominio fue reducido

    while queue:                        # mientras haya arcos por revisar
        xi, xj = queue.popleft()        # saca el siguiente arco (FIFO)

        if revisar(dominios, xi, xj):   # intenta reducir dominio de xi usando xj
            if not dominios[xi]:        # si el dominio quedó vacío → contradicción
                if verbose:
                    r, c = rc(xi)
                    print(f"  Dominio vacío en ({r},{c}) — inconsistencia detectada")
                return False            # retorna False: no hay solución en esta rama

            # El dominio de xi cambió → sus vecinos deben revisarse de nuevo
            r, c = rc(xi)              # obtiene coordenadas de xi
            for xk in peers(r, c):     # para cada vecino xk de xi
                if xk != xj:           # no reagregar el arco que acabamos de procesar
                    queue.append((xk, xi))  # agrega arco xk→xi para re-revisar xk

            podas += 1  # contabiliza esta ronda de poda

    if verbose:
        print(f"  AC-3 completado — {podas} rondas de revisión")
    return True  # todos los dominios son consistentes entre sí


# ─── Backtracking con propagación ────────────────────────────────────────────

def seleccionar_variable(dominios, asignadas):
    # Heurística MRV: elige la variable (celda) no asignada con MENOS opciones
    # Esto reduce el árbol de búsqueda atacando primero las celdas más restringidas

    return min(
        (i for i in range(81) if i not in asignadas),  # solo celdas sin asignar
        key=lambda i: len(dominios[i])                  # ordena por tamaño de dominio
    )
    # min() devuelve el índice cuyo dominio es el más pequeño


def backtrack(dominios, asignadas, pasos):
    # Búsqueda recursiva con retroceso (backtracking)
    # En cada llamada: elige una celda, prueba un valor, propaga, y recursa

    if len(asignadas) == 81:  # todas las celdas tienen valor → solución completa
        return asignadas      # retorna el diccionario con la solución

    xi = seleccionar_variable(dominios, asignadas)  # celda con menor dominio (MRV)
    r, c = rc(xi)                                   # coordenadas de esa celda

    for val in sorted(dominios[xi]):  # prueba cada valor posible en orden
        pasos[0] += 1                 # incrementa contador (lista para pasar por referencia)

        # Copia profunda: no queremos modificar el estado actual si este intento falla
        dominios_copia = copy.deepcopy(dominios)

        # Fija el valor val en la copia del dominio de xi
        dominios_copia[xi] = {val}

        # Copia del diccionario de asignaciones con el nuevo valor
        nueva_asignadas = dict(asignadas)
        nueva_asignadas[xi] = val  # registra la asignación de xi = val

        # Genera los arcos a propagar: todos los vecinos de xi deben revisarse
        # La dirección es (vecino → xi) porque xi acaba de reducir su dominio a {val}
        arcos_iniciales = [(xj, xi) for xj in peers(r, c)]

        # Corre AC-3 solo con esos arcos para propagar el efecto de la asignación
        if ac3(dominios_copia, arcos=arcos_iniciales, verbose=False):

            # Aprovecha inferencias: celdas que quedaron con dominio de tamaño 1
            for i in range(81):
                if i not in nueva_asignadas and len(dominios_copia[i]) == 1:
                    # Esta celda ya tiene un único valor posible → asígnarla gratis
                    nueva_asignadas[i] = next(iter(dominios_copia[i]))

            # Llama recursivamente con el estado actualizado
            resultado = backtrack(dominios_copia, nueva_asignadas, pasos)

            if resultado is not None:  # si la recursión encontró solución
                return resultado       # propaga la solución hacia arriba

    # Ningún valor funcionó para xi → retroceso (backtrack)
    return None


# ─── Interfaz principal ───────────────────────────────────────────────────────

# Puzzle de ejemplo (0 = celda vacía)
PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def inicializar_dominios(puzzle):
    # Crea la estructura inicial de dominios a partir del puzzle dado

    # Cada una de las 81 celdas empieza con dominio {1,2,3,4,5,6,7,8,9}
    dominios = [set(range(1, 10)) for _ in range(81)]

    asignadas = {}  # diccionario {índice: valor} para celdas ya conocidas

    for r in range(9):        # recorre filas
        for c in range(9):    # recorre columnas
            if puzzle[r][c] != 0:          # si la celda tiene valor inicial
                i = idx(r, c)              # calcula su índice lineal
                dominios[i] = {puzzle[r][c]}   # dominio queda reducido a ese valor
                asignadas[i] = puzzle[r][c]    # registra como asignada

    return dominios, asignadas  # devuelve ambas estructuras


def imprimir_tablero(asignadas, titulo="Tablero"):
    # Imprime el tablero en consola con separadores de caja 3x3

    print(f"\n{'─'*25}  {titulo}  {'─'*25}")

    for r in range(9):              # recorre cada fila
        if r in (3, 6):             # antes de la fila 3 y 6 imprime separador horizontal
            print("├───────┼───────┼───────┤")

        fila = ""                   # acumula el texto de la fila

        for c in range(9):          # recorre cada columna
            if c in (3, 6):         # antes de columna 3 y 6 imprime separador vertical
                fila += " │ "

            v = asignadas.get(idx(r, c), 0)  # obtiene valor, o 0 si no está asignada
            fila += str(v) if v else "·"     # muestra número o punto si está vacía

        print(f"  {fila}")          # imprime la fila con sangría

    print("─" * 57)                 # línea inferior


def resolver(puzzle):
    # Función principal que orquesta todo el proceso de resolución

    # Encabezado visual
    print("╔══════════════════════════════════════╗")
    print("║  Propagación de Restricciones — AC-3 ║")
    print("╚══════════════════════════════════════╝\n")

    # Construye dominios iniciales a partir del puzzle
    dominios, asignadas = inicializar_dominios(puzzle)
    imprimir_tablero(asignadas, "Puzzle inicial")  # muestra estado inicial

    # ── Paso 1: propagación pura ──────────────────────────────────────────────
    print("\n[1] Aplicando AC-3 inicial...")

    # Corre AC-3 con todos los arcos del tablero
    if not ac3(dominios, verbose=True):
        print("El puzzle tiene inconsistencia desde el inicio.")
        return  # termina si el puzzle ya es inválido

    # Revisa cuántas celdas quedaron con dominio de tamaño 1 (inferidas sin adivinar)
    inferidas = 0
    for i in range(81):
        if i not in asignadas and len(dominios[i]) == 1:   # celda resuelta por AC-3
            asignadas[i] = next(iter(dominios[i]))         # extrae el único valor posible
            inferidas += 1                                 # contabiliza

    print(f"  Celdas inferidas solo por propagación: {inferidas}")
    imprimir_tablero(asignadas, "Después de AC-3")  # muestra estado tras propagación

    # ── Paso 2: backtracking si quedan celdas sin resolver ────────────────────
    pendientes = 81 - len(asignadas)  # celdas que AC-3 no pudo resolver solo

    if pendientes > 0:
        print(f"\n[2] Quedan {pendientes} celdas — iniciando backtracking + AC-3...")

        pasos = [0]  # lista de un elemento para poder modificarlo dentro de la recursión

        # Llama al backtracking con propagación integrada
        solucion = backtrack(dominios, asignadas, pasos)

        if solucion:
            print(f"  Solución encontrada en {pasos[0]} pasos de backtracking")
            imprimir_tablero(solucion, "Solución final ")
        else:
            print("  No se encontró solución.")  # el puzzle no tiene solución
    else:
        # AC-3 solo fue suficiente para resolver el puzzle completamente
        print("\n Resuelto completamente solo con propagación de restricciones.")
        imprimir_tablero(asignadas, "Solución final ")


# Punto de entrada: solo ejecuta resolver() si se corre este archivo directamente
# (no si se importa como módulo desde otro script)
if __name__ == "__main__":
    resolver(PUZZLE)