#2
#Uniform Cost Search
#Busqueda de Anchura de Costo Uniforme

import heapq # Importa 'heapq' para manejar la cola de prioridad de UCS de forma eficiente

class Graph: # Define la clase 'Graph' para representar el grafo con costos asociados a las aristas
    def __init__(self): # Inicializa el grafo como un diccionario vacío donde cada clave es un nodo y su valor es una lista de tuplas (vecino, costo)
        self.graph = {} # Diccionario para almacenar el grafo, donde cada clave es un nodo y su valor es una lista de tuplas (vecino, costo)
        
    def add_edge(self, start, end, cost): # Método para agregar una arista al grafo, especificando el nodo de inicio, el nodo de destino y el costo asociado a esa arista
        if start not in self.graph: # Si el nodo de inicio no existe en el grafo, lo agrega con una lista vacía para almacenar sus vecinos y costos
            self.graph[start] = [] # Si el nodo de inicio no existe en el grafo, lo agrega con una lista vacía para almacenar sus vecinos y costos
        self.graph[start].append((end, cost)) # Agrega una tupla (vecino, costo) a la lista de vecinos del nodo de inicio, representando la arista desde 'start' hasta 'end' con el costo especificado
        
def ucs(graph, start, goal):  # Función que implementa la búsqueda de costo uniforme (UCS), tomando como parámetros el grafo, el nodo de inicio y el nodo objetivo
    priority_queue = [(0, start)]  # Cola de prioridad para manejar los nodos a explorar, inicializada con el nodo de inicio y un costo inicial de 0 (costo acumulado desde el nodo de inicio hasta el nodo actual)
    visited = set() # Conjunto para rastrear los nodos visitados y evitar ciclos
    
    while priority_queue:  # Mientras la cola de prioridad no esté vacía, continúa explorando
        cost, node = heapq.heappop(priority_queue) # Extrae el nodo con el costo acumulado más bajo de la cola de prioridad, obteniendo tanto el costo como el nodo actual
        
        if node in visited:  # Si el nodo ya ha sido visitado, lo ignora y continúa con la siguiente iteración del ciclo
            continue 
        print(f"Visiting node: {node} with cost: {cost}") # Imprime el nodo que se está visitando y su costo acumulado desde el nodo de inicio, para mostrar el proceso de exploración de UCS
        
        visited.add(node) # Marca el nodo actual como visitado para evitar volver a explorarlo en iteraciones futuras
        
        if node == goal:  # Si el nodo actual es el nodo objetivo, imprime un mensaje indicando que se ha encontrado el objetivo y retorna (puede retornar el costo o el camino, dependiendo de la implementación deseada)
            print("Target found") # Imprime un mensaje indicando que se ha encontrado el nodo objetivo
            return # Retorna para finalizar la función, ya que se ha encontrado el nodo objetivo
        
        if node in graph.graph: # Si el nodo actual tiene vecinos en el grafo, itera sobre ellos para agregar los vecinos no visitados a la cola de prioridad con su costo acumulado actualizado
            for neighbor, edge_cost in graph.graph[node]: # Itera sobre los vecinos del nodo actual, obteniendo tanto el vecino como el costo de la arista que conecta el nodo actual con ese vecino
                if neighbor not in visited: # Si el vecino no ha sido visitado, lo agrega a la cola de prioridad con su costo acumulado actualizado (costo actual + costo de la arista)
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor)) # Agrega el vecino a la cola de prioridad con su costo acumulado actualizado, utilizando 'heappush' para mantener la propiedad de la cola de prioridad basada en el costo acumulado


g=Graph() # Crea una instancia de la clase 'Graph' para construir el grafo con los nodos y aristas especificados
g.add_edge(1,2,1) # Agrega una arista desde el nodo 1 hasta el nodo 2 con un costo de 1
g.add_edge(1,3,4) # Agrega una arista desde el nodo 1 hasta el nodo 3 con un costo de 4
g.add_edge(1,9,5) # Agrega una arista desde el nodo 1 hasta el nodo 9 con un costo de 5
g.add_edge(1,10,3) # Agrega una arista desde el nodo 1 hasta el nodo 10 con un costo de 3
g.add_edge(2,3,2) # Agrega una arista desde el nodo 2 hasta el nodo 3 con un costo de 2
g.add_edge(2,4,4) # Agrega una arista desde el nodo 2 hasta el nodo 4 con un costo de 4
g.add_edge(4,5,1) # Agrega una arista desde el nodo 4 hasta el nodo 5 con un costo de 1
g.add_edge(4,6,2) # Agrega una arista desde el nodo 4 hasta el nodo 6 con un costo de 2
g.add_edge(4,7,3) # Agrega una arista desde el nodo 4 hasta el nodo 7 con un costo de 3
g.add_edge(5,8,2) # Agrega una arista desde el nodo 5 hasta el nodo 8 con un costo de 2

ucs(g, 1, 8) # Llama a la función 'ucs' para realizar la búsqueda de costo uniforme desde el nodo 1 hasta el nodo 8, lo que imprimirá el proceso de exploración y el resultado de la búsqueda (en este caso, se espera encontrar el nodo objetivo 8 y mostrar los nodos visitados con sus costos acumulados)