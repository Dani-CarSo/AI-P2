#6
#Bidirectional Search
#Busqueda Bidireccional

from collections import deque # Importamos deque para usarlo como una cola eficiente

def busqueda_bidireccional(grafo, inicio, destino): # Función que realiza la búsqueda bidireccional en un grafo dado, desde un nodo de inicio hasta un nodo de destino
    if inicio == destino: # Si el nodo de inicio es el mismo que el nodo de destino, simplemente devolvemos una lista con ese nodo
        return [inicio] # Si el nodo de inicio es el mismo que el nodo de destino, simplemente devolvemos una lista con ese nodo

    visitados_inicio  = {inicio: None} # Diccionario para rastrear los nodos visitados desde el inicio, con el nodo como clave y su padre como valor
    visitados_destino = {destino: None} # Diccionario para rastrear los nodos visitados desde el destino, con el nodo como clave y su padre como valor
    frontera_inicio   = deque([inicio]) # Cola para almacenar los nodos a explorar desde el inicio
    frontera_destino  = deque([destino]) # Cola para almacenar los nodos a explorar desde el destino

    def reconstruir_camino(nodo_medio): # Función para reconstruir el camino completo desde el nodo de inicio hasta el nodo de destino a través del nodo medio donde se encontraron las búsquedas
        camino = [] # Lista para almacenar el camino completo
        nodo = nodo_medio # Comenzamos desde el nodo medio donde se encontraron las búsquedas
        while nodo is not None: # Mientras el nodo no sea None, seguimos retrocediendo a través de los padres desde el nodo medio hasta el nodo de inicio
            camino.append(nodo) # Agregamos el nodo actual al camino
            nodo = visitados_inicio[nodo] # Actualizamos el nodo actual al padre del nodo actual en la búsqueda desde el inicio
        camino.reverse() # Invertimos el camino para que esté en el orden correcto desde el nodo de inicio hasta el nodo medio
        nodo = visitados_destino[nodo_medio] # Comenzamos desde el nodo medio donde se encontraron las búsquedas
        while nodo is not None: # Mientras el nodo no sea None, seguimos retrocediendo a través de los padres desde el nodo medio hasta el nodo de destino
            camino.append(nodo) # Agregamos el nodo actual al camino
            nodo = visitados_destino[nodo] # Actualizamos el nodo actual al padre del nodo actual en la búsqueda desde el destino
        return camino # Devolvemos el camino completo desde el nodo de inicio hasta el nodo de destino a través del nodo medio

    def expandir(frontera, visitados_este, visitados_otro):  # Función para expandir la frontera de búsqueda, explorando los vecinos del nodo actual y verificando si se ha encontrado un nodo común entre las dos búsquedas
        for _ in range(len(frontera)):      # Iteramos sobre los nodos en la frontera actual, expandiendo cada nodo y explorando sus vecinos
            nodo = frontera.popleft()      # Sacamos el nodo actual de la frontera para expandirlo
            for vecino in grafo.get(nodo, []): # Iteramos sobre los vecinos del nodo actual, obtenidos del grafo
                if vecino not in visitados_este: # Si el vecino no ha sido visitado en esta búsqueda, lo agregamos a la frontera y lo marcamos como visitado con su nodo padre
                    visitados_este[vecino] = nodo # Marcamos el vecino como visitado en esta búsqueda, con el nodo actual como su padre
                    frontera.append(vecino) # Agregamos el vecino a la frontera para que sea explorado en futuras iteraciones
                if vecino in visitados_otro:    # Si el vecino ya ha sido visitado en la otra búsqueda, significa que hemos encontrado un nodo común entre las dos búsquedas, lo que indica que se ha encontrado un camino desde el nodo de inicio hasta el nodo de destino a través de este nodo común
                    return vecino   # Devolvemos el nodo común encontrado entre las dos búsquedas, lo que indica que se ha encontrado un camino desde el nodo de inicio hasta el nodo de destino a través de este nodo común
        return None # Si no se encuentra ningún nodo común entre las dos búsquedas después de expandir todos los nodos en la frontera, devolvemos None para indicar que no se ha encontrado un camino desde el nodo de inicio hasta el nodo de destino

    while frontera_inicio and frontera_destino: # Mientras haya nodos en ambas fronteras de búsqueda, continuamos expandiendo las fronteras y buscando un nodo común entre las dos búsquedas
        if len(frontera_inicio) <= len(frontera_destino): # Si la frontera de búsqueda desde el inicio tiene menos o igual nodos que la frontera de búsqueda desde el destino, expandimos la frontera desde el inicio
            encuentro = expandir(frontera_inicio, visitados_inicio, visitados_destino) # Expandimos la frontera desde el inicio, pasando la frontera de búsqueda desde el inicio, el diccionario de nodos visitados desde el inicio y el diccionario de nodos visitados desde el destino
        else: # Si la frontera de búsqueda desde el destino tiene menos nodos que la frontera de búsqueda desde el inicio, expandimos la frontera desde el destino
            encuentro = expandir(frontera_destino, visitados_destino, visitados_inicio) # Expandimos la frontera desde el destino, pasando la frontera de búsqueda desde el destino, el diccionario de nodos visitados desde el destino y el diccionario de nodos visitados desde el inicio
        if encuentro: # Si se ha encontrado un nodo común entre las dos búsquedas, reconstruimos el camino completo desde el nodo de inicio hasta el nodo de destino a través del nodo común encontrado
            return reconstruir_camino(encuentro) # Devolvemos el camino completo desde el nodo de inicio hasta el nodo de destino a través del nodo común encontrado

    return None # Si no se encuentra ningún camino desde el nodo de inicio hasta el nodo de destino después de agotar ambas fronteras de búsqueda, devolvemos None para indicar que no se ha encontrado un camino

grafo = {  # Grafo representado como un diccionario de adyacencia, donde cada clave es un nodo y su valor es una lista de nodos vecinos
    'M': ['N', 'O', 'P'], # El nodo 'M' tiene como vecinos a los nodos 'N', 'O' y 'P'
    'N': ['M', 'Q', 'R'],  # El nodo 'N' tiene como vecinos a los nodos 'M', 'Q' y 'R'
    'O': ['M', 'R', 'S'],  # El nodo 'O' tiene como vecinos a los nodos 'M', 'R' y 'S'
    'P': ['M', 'R'],  # El nodo 'P' tiene como vecinos a los nodos 'M' y 'R'
    'Q': ['N', 'R'],  # El nodo 'Q' tiene como vecinos a los nodos 'N' y 'R'
    'R': ['N', 'O', 'P', 'Q', 'S', 'T', 'U', 'V'],   # El nodo 'R' tiene como vecinos a los nodos 'N', 'O', 'P', 'Q', 'S', 'T', 'U' y 'V'
    'S': ['O', 'R', 'V'], # El nodo 'S' tiene como vecinos a los nodos 'O', 'R' y 'V'
    'T': ['R', 'V'], # El nodo 'T' tiene como vecinos a los nodos 'R' y 'V'
    'U': ['R', 'V'], # El nodo 'U' tiene como vecinos a los nodos 'R' y 'V'
    'V': ['R', 'S', 'T', 'U'],  # El nodo 'V' tiene como vecinos a los nodos 'R', 'S', 'T' y 'U'
}

camino = busqueda_bidireccional(grafo, 'M', 'V') # Llamamos a la función de búsqueda bidireccional, pasando el grafo, el nodo de inicio 'M' y el nodo de destino 'V', y almacenamos el resultado en la variable camino
print("Camino encontrado:", camino) # Imprimimos el camino encontrado desde el nodo de inicio 'M' hasta el nodo de destino 'V' utilizando la búsqueda bidireccional, mostrando el resultado en la consola
