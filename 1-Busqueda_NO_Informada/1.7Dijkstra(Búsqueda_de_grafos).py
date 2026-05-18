#7
#Búsqueda de Grafos

# Representamos el grafo como un diccionario de diccionarios:
# cada nodo tiene vecinos y el costo de llegar a ellos
grafo = {
    "A": {"B": 3, "C": 1},   # A se conecta con B (3) y C (1)
    "B": {"A": 3, "C": 7, "D": 5},  # B conectado con varios nodos
    "C": {"A": 1, "B": 7, "D": 2},  # C tiene conexiones
    "D": {"B": 5, "C": 2}    # D conecta con B y C
}

# Nodo inicial
# El usuario elige desde qué nodo empezar
inicio = input("Nodo inicial (A, B, C, D): ").upper()

# Lista de nodos que ya forman parte del árbol
visitados = [inicio]

# Lista donde guardaremos las conexiones del árbol mínimo
aristas_mst = []

#Algoritmo principal de Prim
# Se repite hasta que todos los nodos estén conectados
while len(visitados) < len(grafo):

    # Inicializamos el menor costo encontrado
    menor_peso = float("inf")

    # Guardará la mejor conexión encontrada en esta iteración
    mejor_arista = None


    # Recorremos todos los nodos ya visitados
    for u in visitados:

        # Recorremos sus vecinos
        for v, peso in grafo[u].items():

            # Si el vecino NO está visitado (evita ciclos)
            # y el peso es menor que el mejor encontrado
            if v not in visitados and peso < menor_peso:

                # Actualizamos el mejor costo
                menor_peso = peso

                # Guardamos la mejor conexión (origen, destino, costo)
                mejor_arista = (u, v, peso)


    # Agregar la mejor arista
    u, v, peso = mejor_arista  # desempaquetamos la mejor conexión

    # Marcamos el nuevo nodo como visitado
    visitados.append(v)

    # Guardamos la arista en el árbol final
    aristas_mst.append(mejor_arista)

print("\n Árbol de Expansión Mínima")

# Variable para sumar el costo total del árbol
costo_total = 0

# Recorremos todas las aristas seleccionadas
for u, v, peso in aristas_mst:

    # Imprimimos cada conexión del árbol
    print(u, "→", v, "peso:", peso)

    # Sumamos el costo total
    costo_total += peso

# Mostramos el costo total final del árbol
print("\nCosto total:", costo_total)