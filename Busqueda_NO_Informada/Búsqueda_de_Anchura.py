#1
# Breadth-First Search
#Busqueda en Anchura 


from collections import deque  # Importa 'deque' para manejar la cola BFS de forma eficiente

# Define el grafo como un diccionario de listas de adyacencia
# Cada clave es un nodo y su valor es la lista de sus vecinos (nodos a los que apunta)
graph = {
    'T': ['L', 'N', 'K'],  # Nodo T conecta a L, N y K
    'L': ['O'],             # Nodo L conecta a O
    'N': ['P'],             # Nodo N conecta a P
    'K': ['M'],             # Nodo K conecta a M
    'M': ['V'],             # Nodo M conecta a V
    'O': ['Z'],             # Nodo O conecta a Z
    'P': [],                # Nodo P no tiene vecinos
    'V': ['X'],             # Nodo V conecta a X
    'Z': []                 # Nodo Z no tiene vecinos
}

def bfs(graph, start, goal): # Función que implementa la búsqueda en anchura (BFS)

    if start not in graph or goal not in graph: # Verifica si los nodos de inicio y objetivo existen en el grafo
        print(f"Error: '{start if start not in graph else goal}' no existe en el grafo.")# Si alguno de los nodos no existe, imprime un mensaje de error y retorna None
        return None  # Retorna None para indicar que no se pudo realizar la búsqueda

  
    if start == goal: # Si el nodo de inicio es el mismo que el nodo objetivo, retorna una lista con ese nodo como único elemeto, ya que el camino desde el nodo a sí mismo es simplemente ese nodo
        return [start]  # Retorna una lista con el nodo de inicio como único elemento

    visited = set()  # Conjunto para rastrear los nodos visitados y evitar ciclos

   
    queue = deque([(start, [start])]) # Cola para manejar los nodos a explorar, inicializada con el nodo de inicio y su camino asociado (inicialmente solo el nodo de inicio)

    while queue:  # Mientras la cola no esté vacía, continúa explorando
        node, path = queue.popleft()  # Extrae el primer nodo y su camino asociado de la cola

        if node not in visited:   # Si el nodo no ha sido visitado, lo marca como visitado
            visited.add(node)        # Agrega el nodo a la lista de visitados

            for neighbor in graph.get(node, []): # Itera sobre los vecinos del nodo actual (si no tiene vecinos, devuelve una lista vacía)
                new_path = path + [neighbor]      # Crea un nuevo camino que extiende el camino actual con el vecino

                if neighbor == goal:   # Si el vecino es el nodo objetivo, retorna el nuevo camino que lleva al objetivo
                    return new_path   # Retorna el camino encontrado desde el nodo de inicio hasta el nodo objetivo
                if neighbor not in visited:       # Si el vecino no ha sido visitado, lo agrega a la cola para su exploración futura       
                    queue.append((neighbor, new_path))   # Agrega el vecino y su camino asociado a la cola para ser explorado en iteraciones futuras

    
    print(f"No se encontró camino de '{start}' a '{goal}'.")  # Si la cola se vacía sin encontrar el nodo objetivo, imprime un mensaje indicando que no se encontró un camino y retorna None
    return None  # Retorna None para indicar que no se encontró un camino entre el nodo de inicio y el nodo objetivo

print(bfs(graph, 'T', 'Z')) # Imprime el resultado de la búsqueda en anchura desde el nodo 'T' hasta el nodo 'Z'
print(bfs(graph, 'T', 'P'))  # Imprime el resultado de la búsqueda en anchura desde el nodo 'T' hasta el nodo 'P'
print(bfs(graph, 'T', 'X'))  # Imprime el resultado de la búsqueda en anchura desde el nodo 'T' hasta el nodo 'X'
print(bfs(graph, 'T', 'T')) # Imprime el resultado de la búsqueda en anchura desde el nodo 'T' hasta el nodo 'T' (caso donde el nodo de inicio es el mismo que el nodo objetivo)
