#1
# Breadth-First Search
#Busqueda en Anchura 

from collections import deque 

graph = {
    'T': ['L', 'N', 'K'],  
    'L': ['O'],             
    'N': ['P'],             
    'K': ['M'],            
    'M': ['V'],             
    'O': ['Z'],          
    'P': [],                
    'V': ['X'],                
    'Z': []                 
}

def bfs(graph, start, goal):

    if start not in graph or goal not in graph:
        print(f"Error: '{start if start not in graph else goal}' no existe en el grafo.")
        return None  

  
    if start == goal:
        return [start]  

    visited = set() 

   
    queue = deque([(start, [start])])

    while queue: 
        node, path = queue.popleft()  

        if node not in visited:   
            visited.add(node)        

            for neighbor in graph.get(node, []): 
                new_path = path + [neighbor]      

                if neighbor == goal:   
                    return new_path   
                if neighbor not in visited:              
                    queue.append((neighbor, new_path))   

    
    print(f"No se encontró camino de '{start}' a '{goal}'.")
    return None  

print(bfs(graph, 'T', 'Z')) 
print(bfs(graph, 'T', 'P'))  
print(bfs(graph, 'T', 'X'))  
print(bfs(graph, 'T', 'T')) 
