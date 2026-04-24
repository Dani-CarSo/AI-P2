#2
#Uniform Cost Search
#Busqueda de Anchura de Costo Uniforme

import heapq

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, start, end, cost):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, cost))
        
def ucs(graph, start, goal):
    priority_queue = [(0, start)] 
    visited = set()
    
    while priority_queue: 
        cost, node = heapq.heappop(priority_queue)
        
        if node in visited:
            continue 
        
        visited.add(node)
        
        if node == goal:
            print("Target found")
            return
        
        if node in graph.graph:
            for neighbor, edge_cost in graph.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor))


g=Graph()
g.add_edge(1,2,1)
g.add_edge(1,9,5)
g.add_edge(1,10,3)
g.add_edge(2,3,2)
g.add_edge(2,4,4)
g.add_edge(4,5,1)
g.add_edge(4,6,2)
g.add_edge(4,7,3)
g.add_edge(5,8,2)

ucs(g, 1, 8)