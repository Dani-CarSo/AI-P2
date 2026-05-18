#10
#Búsquedas A* y AO

import heapq #importar el módulo heapq para utilizar una estructura de datos de min-heap en la implementación del algoritmo A* para gestionar la lista abierta (open_list) de nodos a explorar, lo que permite obtener eficientemente el nodo con el menor costo f(n) en cada iteración del algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
from collections import defaultdict #importar el módulo defaultdict de la biblioteca collections para utilizar un diccionario que devuelve un valor predeterminado (en este caso, inf) para claves no existentes en la implementación del algoritmo A* para gestionar los costos g(n) de los nodos explorados, lo que permite manejar eficientemente los costos de los nodos sin necesidad de verificar si una clave existe en el diccionario antes de acceder a su valor, facilitando así la actualización y comparación de costos durante la ejecución del algoritmo A*.
from math import inf #importar la constante inf del módulo math para representar un valor infinito en la implementación del algoritmo A* para inicializar los costos g(n) de los nodos no explorados, lo que permite comparar y actualizar eficientemente los costos de los nodos durante la ejecución del algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.


def astar(graph, start, goal, heuristic): #definir la función astar que implementa el algoritmo A* para encontrar el camino más corto desde un nodo inicial (start) hasta un nodo objetivo (goal) en un grafo ponderado representado por un diccionario (graph) y utilizando una función heurística (heuristic) para estimar el costo restante desde cada nodo hasta el objetivo, lo que permite guiar la búsqueda de manera eficiente hacia la solución óptima en el espacio de búsqueda definido por el grafo y la función heurística.
  
    open_list = []          # min-heap
    heapq.heappush(open_list, (0, start)) #inicializar la lista abierta (open_list) como un min-heap utilizando el módulo heapq para gestionar los nodos a explorar en el algoritmo A*, comenzando con el nodo inicial (start) con un costo f(n) de 0, lo que permite obtener eficientemente el nodo con el menor costo f(n) en cada iteración del algoritmo A* para encontrar el camino más corto desde el nodo inicial hasta el nodo objetivo en un grafo ponderado.

    g = defaultdict(lambda: inf) #inicializar el diccionario g utilizando defaultdict para gestionar los costos g(n) de los nodos explorados en el algoritmo A*, donde cada nodo no explorado tendrá un costo inicial de infinito (inf), lo que permite comparar y actualizar eficientemente los costos de los nodos durante la ejecución del algoritmo A* para encontrar el camino más corto desde el nodo inicial hasta el nodo objetivo en un grafo ponderado.
    g[start] = 0  #establecer el costo g(n) del nodo inicial (start) a 0 en el diccionario g para indicar que el costo desde el nodo inicial hasta sí mismo es cero, lo que permite iniciar la búsqueda del algoritmo A* con el nodo inicial como punto de partida para encontrar el camino más corto hasta el nodo objetivo en un grafo ponderado.

    parent = {start: None} #inicializar el diccionario parent para gestionar los nodos padres de cada nodo explorado en el algoritmo A*, donde el nodo inicial (start) no tiene un nodo padre (None), lo que permite reconstruir el camino desde el nodo objetivo hasta el nodo inicial una vez que se encuentra la solución óptima en el espacio de búsqueda definido por el grafo y la función heurística.
    closed = set()  #inicializar el conjunto closed para gestionar los nodos ya explorados en el algoritmo A*, lo que permite evitar la exploración redundante de nodos y mejorar la eficiencia de la búsqueda al mantener un registro de los nodos que ya han sido procesados durante la ejecución del algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.

    while open_list:   #mientras la lista abierta (open_list) no esté vacía, lo que indica que aún hay nodos por explorar en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado, se continúa con el proceso de exploración y expansión de nodos en cada iteración del algoritmo A*.
        f_curr, curr = heapq.heappop(open_list)    #obtener el nodo con el menor costo f(n) de la lista abierta (open_list) utilizando heapq.heappop para gestionar eficientemente los nodos a explorar en el algoritmo A*, lo que permite obtener el nodo más prometedor en cada iteración del algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.

        if curr in closed:  #si el nodo actual (curr) ya ha sido explorado (está en el conjunto closed), se omite su procesamiento y se continúa con la siguiente iteración del bucle while para obtener el siguiente nodo con el menor costo f(n) de la lista abierta (open_list) en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado, lo que evita la exploración redundante de nodos y mejora la eficiencia de la búsqueda.
            continue   #si el nodo actual (curr) ya ha sido explorado (está en el conjunto closed), se omite su procesamiento y se continúa con la siguiente iteración del bucle while para obtener el siguiente nodo con el menor costo f(n) de la lista abierta (open_list) en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado, lo que evita la exploración redundante de nodos y mejora la eficiencia de la búsqueda.
        closed.add(curr)  #agregar el nodo actual (curr) al conjunto closed para marcarlo como explorado en el algoritmo A*, lo que permite evitar la exploración redundante de nodos y mejorar la eficiencia de la búsqueda al mantener un registro de los nodos que ya han sido procesados durante la ejecución del algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.

        if curr == goal:  #si el nodo actual (curr) es igual al nodo objetivo (goal), se ha encontrado la solución óptima en el espacio de búsqueda definido por el grafo y la función heurística, por lo que se devuelve el costo g(n) del nodo objetivo y el camino reconstruido desde el nodo objetivo hasta el nodo inicial utilizando la función _reconstruct para mostrar la solución encontrada por el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
            return g[goal], _reconstruct(parent, goal)  #si el nodo actual (curr) es igual al nodo objetivo (goal), se ha encontrado la solución óptima en el espacio de búsqueda definido por el grafo y la función heurística, por lo que se devuelve el costo g(n) del nodo objetivo y el camino reconstruido desde el nodo objetivo hasta el nodo inicial utilizando la función _reconstruct para mostrar la solución encontrada por el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.

        for neighbor, cost in graph.get(curr, []):  #iterar por los vecinos del nodo actual (curr) y sus costos asociados en el grafo utilizando graph.get(curr, []) para obtener la lista de vecinos y costos, lo que permite explorar los nodos adyacentes al nodo actual en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
            tentative_g = g[curr] + cost  #calcular el costo g(n) tentativo para el vecino actual (neighbor) sumando el costo g(n) del nodo actual (curr) y el costo de la arista que conecta el nodo actual con el vecino, lo que permite evaluar si se ha encontrado un camino más corto hacia el vecino en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
            if tentative_g < g[neighbor]:   #si el costo g(n) tentativo para el vecino actual (neighbor) es menor que el costo g(n) registrado en el diccionario g para ese vecino, se ha encontrado un camino más corto hacia el vecino, por lo que se actualiza el costo g(n) del vecino en el diccionario g, se establece el nodo actual como su nodo padre en el diccionario parent, y se calcula el costo f(n) para el vecino utilizando la función heurística para agregarlo a la lista abierta (open_list) con su nuevo costo f(n) para continuar la búsqueda del algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
                g[neighbor] = tentative_g  #actualizar el costo g(n) del vecino actual (neighbor) en el diccionario g con el costo g(n) tentativo, lo que indica que se ha encontrado un camino más corto hacia ese vecino en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
                parent[neighbor] = curr  #establecer el nodo actual (curr) como el nodo padre del vecino actual (neighbor) en el diccionario parent para permitir la reconstrucción del camino desde el nodo objetivo hasta el nodo inicial una vez que se encuentra la solución óptima en el espacio de búsqueda definido por el grafo y la función heurística en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
                f = tentative_g + heuristic.get(neighbor, 0)  #calcular el costo f(n) para el vecino actual (neighbor) sumando el costo g(n) tentativo y la estimación heurística del costo restante desde el vecino hasta el nodo objetivo utilizando heuristic.get(neighbor, 0) para obtener la estimación heurística, lo que permite guiar la búsqueda de manera eficiente hacia la solución óptima en el espacio de búsqueda definido por el grafo y la función heurística en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
                heapq.heappush(open_list, (f, neighbor))  # agregar el vecino actual (neighbor) a la lista abierta (open_list) con su costo f(n) calculado utilizando heapq.heappush para gestionar eficientemente los nodos a explorar en el algoritmo A*, lo que permite obtener el nodo más prometedor en cada iteración del algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.

    return inf, None  #si la lista abierta (open_list) se vacía sin encontrar el nodo objetivo (goal), se devuelve un costo infinito (inf) y None para indicar que no se ha encontrado una solución en el espacio de búsqueda definido por el grafo y la función heurística en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.


def _reconstruct(parent, node):  #definir la función _reconstruct que reconstruye el camino desde un nodo objetivo hasta un nodo inicial utilizando el diccionario parent que gestiona los nodos padres de cada nodo explorado en el algoritmo A*, lo que permite mostrar la solución encontrada por el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
    path = []  #lista para almacenar el camino reconstruido desde el nodo objetivo hasta el nodo inicial utilizando el diccionario parent para seguir los nodos padres en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
    while node is not None:  #mientras el nodo actual (node) no sea None, lo que indica que se ha llegado al nodo inicial (start) durante la reconstrucción del camino utilizando el diccionario parent en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado, se continúa agregando los nodos al camino reconstruido.
        path.append(node)  # agregar el nodo actual (node) al camino reconstruido
        node = parent[node]  #actualizar el nodo actual (node) al nodo padre del nodo actual utilizando el diccionario parent para seguir los nodos padres durante la reconstrucción del camino en el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado, lo que permite mostrar la solución encontrada por el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado.
    return path[::-1] # devolver el camino reconstruido desde el nodo objetivo hasta el nodo inicial en orden inverso para mostrar la solución encontrada por el algoritmo A* para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo en un grafo ponderado, lo que permite presentar la solución de manera clara y comprensible.


class AONode:  #    definir la clase AONode que representa un nodo en un grafo AND-OR para la implementación del algoritmo AO* para encontrar la solución óptima en un espacio de búsqueda definido por un grafo AND-OR, donde cada nodo tiene un nombre, una heurística (h), un costo (cost), una bandera de si es un nodo objetivo (is_goal), una bandera de si está resuelto (solved), una lista de hijos (children) y una referencia al mejor arco (best_arc) para gestionar la estructura del grafo AND-OR y facilitar la búsqueda de la solución óptima utilizando el algoritmo AO* para encontrar la solución óptima en un espacio de búsqueda definido por un grafo AND-OR.           
    """Nodo de un grafo AND-OR."""
    def __init__(self, name, h=0, is_goal=False):
        self.name     = name
        self.h        = h           
        self.cost     = h          
        self.is_goal  = is_goal
        self.solved   = is_goal
        self.children = []          
        self.best_arc = None

    def __repr__(self):
        return f"AONode({self.name}, cost={self.cost:.1f})"


class ArcAO:
    
    def __init__(self, nodes, cost=0, arc_type='OR'):
        self.nodes    = nodes       
        self.cost     = cost
        self.arc_type = arc_type

    def arc_cost(self):
        if self.arc_type == 'AND':
            return self.cost + sum(n.cost for n in self.nodes)
        else:  # OR
            return self.cost + min(n.cost for n in self.nodes)

    def is_solved(self):
        if self.arc_type == 'AND':
            return all(n.solved for n in self.nodes)
        else:
            return any(n.solved for n in self.nodes)


def aostar(root: AONode) -> AONode:
  
    def expand_best(node):
        if node.solved or not node.children:
            return

        
        best = min(node.children, key=lambda a: a.arc_cost())
        node.best_arc = best
        node.cost     = best.arc_cost()
        node.solved   = best.is_solved()

        
        for child in best.nodes:
            if not child.solved:
                expand_best(child)

        # Propagar hacia atrás
        best = min(node.children, key=lambda a: a.arc_cost())
        node.best_arc = best
        node.cost     = best.arc_cost()
        node.solved   = best.is_solved()

    expand_best(root)
    return root


def print_solution(node, indent=0):
    prefix = "  " * indent
    status = "✓" if node.solved else "?"
    print(f"{prefix}[{status}] {node.name}  cost={node.cost:.1f}")
    if node.best_arc:
        atype = node.best_arc.arc_type
        print(f"{prefix}  └─({atype})")
        for child in node.best_arc.nodes:
            print_solution(child, indent + 2)


if __name__ == "__main__":

  
    print("=== A* ===")
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': [],
    }
    heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
    cost, path = astar(graph, 'A', 'D', heuristic)
    print(f"Costo: {cost}, Camino: {path}")
   

    print("\n=== AO* ===")
    A  = AONode('A',  h=5)
    B  = AONode('B',  h=4)
    C  = AONode('C',  h=2)
    D  = AONode('D',  h=3)
    E  = AONode('E',  h=0, is_goal=True)
    F  = AONode('F',  h=0, is_goal=True)
    G  = AONode('G',  h=0, is_goal=True)


    A.children = [
        ArcAO([B],    cost=1, arc_type='OR'),
        ArcAO([C, D], cost=1, arc_type='AND'),
    ]
    B.children  = [ArcAO([E],    cost=2, arc_type='OR')]
    C.children  = [ArcAO([F],    cost=1, arc_type='OR')]
    D.children  = [ArcAO([G],    cost=1, arc_type='OR')]

    root = aostar(A)
    print_solution(root)