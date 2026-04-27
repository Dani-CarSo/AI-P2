#10
#Búsquedas A* y AO

import heapq
from collections import defaultdict
from math import inf


def astar(graph, start, goal, heuristic):
    """
    graph   : dict  {nodo: [(vecino, costo), ...]}
    heuristic: dict {nodo: h_valor}
    retorna : (costo_total, [camino]) o (inf, None)
    """
    open_list = []          # min-heap
    heapq.heappush(open_list, (0, start))

    g = defaultdict(lambda: inf)
    g[start] = 0

    parent = {start: None}
    closed = set()

    while open_list:
        f_curr, curr = heapq.heappop(open_list)

        if curr in closed:
            continue
        closed.add(curr)

        if curr == goal:
            return g[goal], _reconstruct(parent, goal)

        for neighbor, cost in graph.get(curr, []):
            tentative_g = g[curr] + cost
            if tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                parent[neighbor] = curr
                f = tentative_g + heuristic.get(neighbor, 0)
                heapq.heappush(open_list, (f, neighbor))

    return inf, None


def _reconstruct(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


class AONode:
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