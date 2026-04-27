#9
#Búsqueda Voraz Primero el Mejor
#Greedy Best-First Search

import heapq

graph = {
    1: [(2, 15), (3, 4)],
    2: [(4, 3), (6, 7), (7, 10)],
    3: [(4, 2), (5, 6)],
    4: [(5, 4)],
    5: [(6, 4)],
    6: [(7, 5)],
    7: []
}

heuristic = {
    1: 16,
    2: 11,
    3: 10,
    4: 7,
    5: 9,
    6: 4,
    7: 0
}

def greedy_best_first_search(graph, heuristic, start, goal): 
    visited = set()
    priority_queue = [(heuristic[start], start, [start])]

    while priority_queue:
        h_value, current_node, path = heapq.heappop(priority_queue) 
        
        if current_node in visited:
            continue
        visited.add(current_node)
        print(f"Visitando nodo: {current_node} con heurística: {h_value}")

        if current_node == goal:  
            print(f"Camino encontrado: {' -> '.join(map(str, path))} con costo heurístico: {h_value}")
            return path 

        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    print("No se encontró un camino al objetivo.")
    return None 


source_node = 1  
target = 7
result = greedy_best_first_search(graph, heuristic, source_node, target)