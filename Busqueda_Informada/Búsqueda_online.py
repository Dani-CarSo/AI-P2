#16
#Búsqueda Online

import random

# Grafo desconocido parcialmente (el agente lo "descubre")
grafo_real = { 
    'A': ['B', 'C'], # El agente solo conoce A inicialmente
    'B': ['A', 'D', 'E'], # El agente descubre B al llegar a A
    'C': ['A', 'F'],  # El agente descubre C al llegar a A
    'D': ['B'],  # El agente descubre D al llegar a B
    'E': ['B', 'G'], # El agente descubre E al llegar a B
    'F': ['C'], # El agente descubre F al llegar a C
    'G': []  # El agente descubre G al llegar a E
}

def obtener_vecinos(nodo): # Función que simula el descubrimiento de vecinos al llegar a un nodo
    # Simula que el agente descubre vecinos al llegar
    return grafo_real.get(nodo, []) # El agente solo conoce los vecinos del nodo actual

def busqueda_online(inicio, objetivo): # Búsqueda online sin conocimiento previo del grafo
    actual = inicio # El agente comienza en el nodo de inicio
    visitados = set() # Para evitar ciclos
    camino = [actual] # Camino recorrido

    while actual != objetivo: # Mientras no se alcance el objetivo
        visitados.add(actual) # Marcar el nodo actual como visitado

        vecinos = obtener_vecinos(actual) # Obtener vecinos del nodo actual (descubrir el grafo)
        no_visitados = [n for n in vecinos if n not in visitados] # Filtrar vecinos no visitados

        if no_visitados: # Si hay vecinos no visitados, elegir uno al azar para avanzar
            # Elegir uno no visitado (decisión local)
            siguiente = random.choice(no_visitados) # Elegir aleatoriamente entre los no visitados
        elif vecinos: # Si todos los vecinos han sido visitados, elegir uno al azar para retroceder (backtracking)
            # Si todos visitados, moverse aleatoriamente (backtracking simple)
            siguiente = random.choice(vecinos) # Elegir aleatoriamente entre los vecinos (incluso si ya fueron visitados)
        else: # Si no hay vecinos, el agente está atrapado (no hay caminos disponibles)
            print("No hay más caminos disponibles") # El agente no puede avanzar ni retroceder
            return None # Terminar la búsqueda

        camino.append(siguiente) # Agregar el siguiente nodo al camino recorrido
        actual = siguiente # Moverse al siguiente nodo

    return camino # Devolver el camino encontrado al objetivo

# Ejecutar
camino = busqueda_online('A', 'G') # Buscar un camino desde A hasta G
print("Camino encontrado:", camino) # Imprimir el camino encontrado al objetivo G