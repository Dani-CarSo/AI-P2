#22
#Búsqueda Local: Mínimos-Conflictos

import random
 
# Configuración
 
N = 8            # Número de reinas (y tamaño del tablero N×N)
MAX_ITER = 1000  # Intentos máximos por ejecución antes de reiniciar
MAX_REINICIOS = 100  # Número máximo de reinicios completos
 
# Estado: lista de longitud N
#   índice  → fila de la reina
#   valor   → columna donde está colocada
# Garantiza una reina por fila desde el inicio.

 
def generar_estado() -> list[int]:
    estado = list(range(N))
    random.shuffle(estado)
    return estado
 

# Función de conflictos

 
def contar_conflictos(estado: list[int], fila: int, col: int) -> int:

    total = 0
    for f, c in enumerate(estado):
        if f == fila:
            continue  # No se compara con sí misma
        if c == col or abs(f - fila) == abs(c - col):
            total += 1
    return total
 
 
def total_conflictos_tablero(estado: list[int]) -> int:
   
    return sum(contar_conflictos(estado, i, estado[i]) for i in range(N)) // 2
 
# Algoritmo Min-Conflicts

 
def min_conflicts(max_iter: int = MAX_ITER) -> list[int] | None:
  
    estado = generar_estado()
 
    for iteracion in range(max_iter):
 
        # ── 1. Verificar si es solución ──────────────────────────────────
        reinas_conflictuadas = [
            i for i in range(N)
            if contar_conflictos(estado, i, estado[i]) > 0
        ]
 
        if not reinas_conflictuadas:
            return estado  # ¡Solución encontrada!
 
        # ── 2. Seleccionar una reina conflictuada al azar ─────────────────
        fila = random.choice(reinas_conflictuadas)
 
        # ── 3. Encontrar la columna con menos conflictos ──────────────────
        min_conf = float("inf")
        mejores_columnas = []
 
        for col in range(N):
            c = contar_conflictos(estado, fila, col)
            if c < min_conf:
                min_conf = c
                mejores_columnas = [col]
            elif c == min_conf:
                mejores_columnas.append(col)
 
        # Mover la reina; si hay empate, elige al azar (diversificación)
        estado[fila] = random.choice(mejores_columnas)
 
    return None  # No se encontró solución en este intento
 
 
# ─────────────────────────────────────────────
# Visualización del tablero
# ─────────────────────────────────────────────
 
def imprimir_tablero(estado: list[int]) -> None:
  
    separador = "+" + ("---+" * N)
    for fila, col_reina in enumerate(estado):
        print(separador)
        fila_str = "|"
        for col in range(N):
            fila_str += " Q |" if col == col_reina else " . |"
        print(fila_str)
    print(separador)
 
 
# ─────────────────────────────────────────────
# Punto de entrada
# ─────────────────────────────────────────────
 
def main() -> None:
    print(f" Problema de las {N}-Reinas            ")

    solucion = None
 
    for reinicio in range(1, MAX_REINICIOS + 1):
        solucion = min_conflicts()
        if solucion is not None:
            print(f"✔ Solución encontrada en el reinicio #{reinicio}\n")
            break
        print(f"  Reinicio #{reinicio}: sin solución, intentando de nuevo...")
 
    if solucion:
        print(f"Estado (columna por fila): {solucion}")
        print(f"Conflictos totales:        {total_conflictos_tablero(solucion)}\n")
        imprimir_tablero(solucion)
    else:
        print(" No se encontró solución después de todos los reinicios.")
 
 
if __name__ == "__main__":
    main()
 