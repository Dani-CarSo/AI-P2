#6
#Bidirectional Search
#Busqueda Bidireccional

from collections import deque

def busqueda_bidireccional(grafo, inicio, destino):
    if inicio == destino:
        return [inicio]

    visitados_inicio  = {inicio: None}
    visitados_destino = {destino: None}
    frontera_inicio   = deque([inicio])
    frontera_destino  = deque([destino])

    def reconstruir_camino(nodo_medio):
        camino = []
        nodo = nodo_medio
        while nodo is not None:
            camino.append(nodo)
            nodo = visitados_inicio[nodo]
        camino.reverse()
        nodo = visitados_destino[nodo_medio]
        while nodo is not None:
            camino.append(nodo)
            nodo = visitados_destino[nodo]
        return camino

    def expandir(frontera, visitados_este, visitados_otro):
        for _ in range(len(frontera)):
            nodo = frontera.popleft()
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados_este:
                    visitados_este[vecino] = nodo
                    frontera.append(vecino)
                if vecino in visitados_otro:
                    return vecino
        return None

    while frontera_inicio and frontera_destino:
        if len(frontera_inicio) <= len(frontera_destino):
            encuentro = expandir(frontera_inicio, visitados_inicio, visitados_destino)
        else:
            encuentro = expandir(frontera_destino, visitados_destino, visitados_inicio)
        if encuentro:
            return reconstruir_camino(encuentro)

    return None

grafo = {
    'M': ['N', 'O', 'P'],
    'N': ['M', 'Q', 'R'],
    'O': ['M', 'R', 'S'],
    'P': ['M', 'R'],
    'Q': ['N', 'R'],
    'R': ['N', 'O', 'P', 'Q', 'S', 'T', 'U', 'V'],  
    'S': ['O', 'R', 'V'],
    'T': ['R', 'V'],
    'U': ['R', 'V'],
    'V': ['R', 'S', 'T', 'U'],
}

camino = busqueda_bidireccional(grafo, 'M', 'V')
print("Camino encontrado:", camino)
