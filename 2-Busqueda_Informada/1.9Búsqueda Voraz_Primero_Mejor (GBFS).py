#9
#Búsqueda Voraz Primero el Mejor
#Greedy Best-First Search

import heapq #importar el módulo heapq para utilizar una cola de prioridad en la implementación de la búsqueda voraz primero el mejor

graph = { #definir el grafo como un diccionario donde cada clave es un nodo y su valor es una lista de tuplas que representan los vecinos y el costo de llegar a ellos
    1: [(2, 15), (3, 4)], #nodo 1 tiene vecinos 2 y 3 con costos 15 y 4 respectivamente
    2: [(4, 3), (6, 7), (7, 10)], #nodo 2 tiene vecinos 4, 6 y 7 con costos 3, 7 y 10 respectivamente
    3: [(4, 2), (5, 6)], #nodo 3 tiene vecinos 4 y 5 con costos 2 y 6 respectivamente
    4: [(5, 4)], #nodo 4 tiene vecino 5 con costo 4
    5: [(6, 4)], #nodo 5 tiene vecino 6 con costo 4
    6: [(7, 5)], #nodo 6 tiene vecino 7 con costo 5
    7: [] #nodo 7 no tiene vecinos
}

heuristic = {  #definir la función heurística como un diccionario donde cada clave es un nodo y su valor es una estimación del costo para llegar al objetivo desde ese nodo
    1: 16, #nodo 1 tiene una heurística de 16 para llegar al objetivo
    2: 11, #nodo 2 tiene una heurística de 11 para llegar al objetivo
    3: 10, #nodo 3 tiene una heurística de 10 para llegar al objetivo
    4: 7,  #nodo 4 tiene una heurística de 7 para llegar al objetivo
    5: 9,  #nodo 5 tiene una heurística de 9 para llegar al objetivo
    6: 4,  #nodo 6 tiene una heurística de 4 para llegar al objetivo
    7: 0   #nodo 7 tiene una heurística de 0 para llegar al objetivo
}

def greedy_best_first_search(graph, heuristic, start, goal): #definir la función de búsqueda voraz primero el mejor que toma como argumentos el grafo, la función heurística, el nodo de inicio y el nodo objetivo
    visited = set() #inicializar un conjunto para rastrear los nodos visitados y evitar ciclos en la búsqueda#
    priority_queue = [(heuristic[start], start, [start])] #inicializar una cola de prioridad con una tupla que contiene la heurística del nodo de inicio, el nodo de inicio y una lista que representa el camino recorrido hasta ahora (inicialmente solo el nodo de inicio)

    while priority_queue: #mientras la cola de prioridad no esté vacía, continuar con la búsqueda
        h_value, current_node, path = heapq.heappop(priority_queue)  #extraer el nodo con la menor heurística de la cola de prioridad para explorar ese nodo en esta iteración
        
        if current_node in visited: #si el nodo actual ya ha sido visitado, omitirlo para evitar ciclos y continuar con la siguiente iteración del ciclo
            continue #omitir el nodo actual si ya ha sido visitado para evitar ciclos en la búsqueda y continuar con la siguiente iteración del ciclo
        visited.add(current_node) #marcar el nodo actual como visitado para evitar volver a explorarlo en futuras iteraciones de la búsqueda
        print(f"Visitando nodo: {current_node} con heurística: {h_value}") #imprimir el nodo actual que se está visitando junto con su valor heurístico para mostrar el progreso de la búsqueda

        if current_node == goal:  #si el nodo actual es el nodo objetivo, se ha encontrado un camino exitoso y se puede imprimir el camino encontrado junto con su costo heurístico antes de devolver el camino como resultado de la función
            print(f"Camino encontrado: {' -> '.join(map(str, path))} con costo heurístico: {h_value}")  #imprimir el camino encontrado desde el nodo de inicio hasta el nodo objetivo junto con su costo heurístico para mostrar el resultado de la búsqueda voraz primero el mejor
            return path #devolver el camino encontrado como resultado de la función si se ha llegado al nodo objetivo para finalizar la búsqueda exitosamente

        for neighbor, cost in graph.get(current_node, []):  #iterar a través de los vecinos del nodo actual utilizando el método get para obtener la lista de vecinos y sus costos, proporcionando una lista vacía como valor predeterminado si el nodo no tiene vecinos
            if neighbor not in visited: #si el vecino no ha sido visitado, agregarlo a la cola de prioridad para su exploración futura, calculando su valor heurístico y actualizando el camino recorrido hasta ese vecino
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))  #agregar el vecino a la cola de prioridad con su valor heurístico, el nodo vecino y el camino actualizado que incluye el vecino para su exploración futura en la búsqueda voraz primero el mejor

    print("No se encontró un camino al objetivo.")  #imprimir un mensaje indicando que no se encontró un camino al objetivo después de agotar todas las opciones en la cola de prioridad sin llegar al nodo objetivo para mostrar el resultado de la búsqueda voraz primero el mejor cuando no se encuentra una solución
    return None #devolver None como resultado de la función si no se encontró un camino al objetivo después de agotar todas las opciones en la cola de prioridad para indicar que la búsqueda voraz primero el mejor no tuvo éxito en encontrar una solución


source_node = 1  #definir el nodo de inicio para la búsqueda voraz primero el mejor, que es el nodo 1 en este caso
target = 7  #definir el nodo objetivo para la búsqueda voraz primero el mejor, que es el nodo 7 en este caso
result = greedy_best_first_search(graph, heuristic, source_node, target)  #ejecutar la función de búsqueda voraz primero el mejor con el grafo, la función heurística, el nodo de inicio y el nodo objetivo definidos para encontrar un camino desde el nodo de inicio hasta el nodo objetivo utilizando esta estrategia de búsqueda informada