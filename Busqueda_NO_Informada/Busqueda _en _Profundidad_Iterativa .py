#5
#Iterative Deepening Depth-First Search (IDDFS)
#Busqueda en Profundidad Iterativa 

class Vertice: #Clase para representar un vértice en el grafo
    def __init__(self, i): #Inicializa el vértice con un identificador, un estado de visitado, un padre y una lista de vecinos
        self.id = i  #Identificador del vértice
        self.visitado = False #Indica si el vértice ha sido visitado durante la búsqueda
        self.padre = None  #Referencia al vértice padre en la ruta de búsqueda
        self.vecinos = []  #Lista de vecinos del vértice, es decir, los vértices adyacentes a este vértice

    def agregarVecino(self, v):  #Agrega un vecino a la lista de vecinos del vértice, asegurándose de no agregar duplicados
        if v not in self.vecinos: #Verifica si el vecino ya está en la lista de vecinos para evitar duplicados
            self.vecinos.append(v) #Agrega el vecino a la lista de vecinos del vértice


class Grafica: #Clase para representar un grafo utilizando una estructura de diccionario para almacenar los vértices
    def __init__(self): #Inicializa el grafo con un diccionario vacío para almacenar los vértices, donde la clave es el identificador del vértice y el valor es una instancia de la clase Vertice
        self.vertices = {} #Diccionario para almacenar los vértices del grafo, donde la clave es el identificador del vértice y el valor es una instancia de la clase Vertice

    def agregarVertice(self, v): #Agrega un vértice al grafo, verificando si el vértice ya existe para evitar duplicados
        if v not in self.vertices:  #Verifica si el vértice ya existe en el grafo para evitar duplicados
            self.vertices[v] = Vertice(v) #Agrega el vértice al diccionario de vértices del grafo, utilizando el identificador del vértice como clave y una instancia de la clase Vertice como valor

    def agregarArista(self, a, b):  #Agrega una arista entre dos vértices en el grafo, verificando si ambos vértices existen antes de agregar la arista
        if a in self.vertices and b in self.vertices: #Verifica si ambos vértices existen en el grafo antes de agregar la arista
            self.vertices[a].agregarVecino(b) #Agrega el vértice b como vecino del vértice a
            self.vertices[b].agregarVecino(a) #Agrega el vértice a como vecino del vértice b para mantener la simetría en el grafo no dirigido

    def resetVisitados(self): #Reinicia el estado de visitado y el padre de todos los vértices en el grafo, estableciendo visitado en False y padre en None para cada vértice
        for v in self.vertices: #Itera sobre todos los vértices en el grafo
            self.vertices[v].visitado = False #Reinicia el estado de visitado del vértice a False, indicando que no ha sido visitado durante la búsqueda
            self.vertices[v].padre = None #Reinicia la referencia al padre del vértice a None, indicando que no tiene un padre asignado en la ruta de búsqueda

    def DLS(self, nodo, meta, limite, profundidad=0): #Función recursiva para realizar la búsqueda en profundidad limitada (DLS), donde nodo es el vértice actual, meta es el vértice objetivo, limite es la profundidad máxima permitida y profundidad es la profundidad actual en la recursión
        self.vertices[nodo].visitado = True #Marca el vértice actual como visitado para evitar ciclos durante la búsqueda

        if nodo == meta: #Si el vértice actual es el vértice objetivo, se ha encontrado la solución y se devuelve una lista que contiene el vértice actual como parte del camino hacia la solución
            return [nodo] #Devuelve una lista que contiene el vértice actual como parte del camino hacia la solución

        if profundidad >= limite: #Si la profundidad actual ha alcanzado o superado el límite de profundidad permitido, se detiene la búsqueda en esta rama y se devuelve None para indicar que no se encontró la solución en esta rama
            return None #Devuelve None para indicar que no se encontró la solución en esta rama debido a que se alcanzó el límite de profundidad permitido 

        for vecino in self.vertices[nodo].vecinos: #Itera sobre los vecinos del vértice actual para continuar la búsqueda en profundidad limitada (DLS) en cada vecino
            if not self.vertices[vecino].visitado: #Si el vecino no ha sido visitado, se marca el vecino como visitado, se establece el vértice actual como el padre del vecino para mantener la referencia en la ruta de búsqueda, y se realiza una llamada recursiva a DLS para continuar la búsqueda en profundidad limitada (DLS) en el vecino 
                self.vertices[vecino].padre = nodo  #Establece el vértice actual como el padre del vecino para mantener la referencia en la ruta de búsqueda
                resultado = self.DLS(vecino, meta, limite, profundidad + 1) #Realiza una llamada recursiva a DLS para continuar la búsqueda en profundidad limitada (DLS) en el vecino, incrementando la profundidad actual en 1
                if resultado is not None: #Si se encontró la solución en la llamada recursiva a DLS, se devuelve una lista que contiene el vértice actual concatenado con el resultado de la llamada recursiva, lo que representa el camino hacia la solución desde el vértice actual hasta el vértice objetivo
                    return [nodo] + resultado #Devuelve una lista que contiene el vértice actual concatenado con el resultado de la llamada recursiva, lo que representa el camino hacia la solución desde el vértice actual hasta el vértice objetivo

        return None #Devuelve None para indicar que no se encontró la solución en esta rama después de explorar todos los vecinos del vértice actual

    def IDDFS(self, inicio, meta, limite_max=10): #Función para realizar la búsqueda en profundidad iterativa (IDDFS), donde inicio es el vértice de inicio, meta es el vértice objetivo y limite_max es la profundidad máxima permitida para la búsqueda iterativa
        if inicio not in self.vertices or meta not in self.vertices: #Verifica si el vértice de inicio o el vértice objetivo no existen en el grafo, y si es así, se imprime un mensaje de error y se devuelve None para indicar que no se puede realizar la búsqueda
            print(f"Error: nodo no existe en el grafo.") #Imprime un mensaje de error indicando que el nodo no existe en el grafo
            return None #Devuelve None para indicar que no se puede realizar la búsqueda debido a que el nodo de inicio o el nodo objetivo no existen en el grafo

        if inicio == meta: #Si el vértice de inicio es el mismo que el vértice objetivo, se ha encontrado la solución y se devuelve una lista que contiene el vértice de inicio como parte del camino hacia la solución
            return [inicio] #Devuelve una lista que contiene el vértice de inicio como parte del camino hacia la solución, ya que el vértice de inicio es el mismo que el vértice objetivo

        for limite in range(limite_max + 1):  #Itera sobre los límites de profundidad desde 0 hasta el límite máximo permitido para realizar la búsqueda en profundidad iterativa (IDDFS) en cada límite de profundidad
            print(f"  Intentando con límite de profundidad: {limite}") #Imprime un mensaje indicando el límite de profundidad actual que se está intentando en la búsqueda en profundidad iterativa (IDDFS)
            self.resetVisitados() #Reinicia el estado de visitado y el padre de todos los vértices en el grafo antes de cada intento de búsqueda en profundidad limitada (DLS) para asegurarse de que cada intento comience con un estado limpio

            resultado = self.DLS(inicio, meta, limite) #Realiza una llamada a la función DLS para realizar la búsqueda en profundidad limitada (DLS) con el límite de profundidad actual, utilizando el vértice de inicio, el vértice objetivo y el límite de profundidad como argumentos

            if resultado is not None: #Si se encontró la solución en la llamada a DLS, se imprime un mensaje indicando que se encontró la solución en el límite de profundidad actual y se devuelve el resultado, que es una lista que representa el camino hacia la solución desde el vértice de inicio hasta el vértice objetivo
                print(f" Encontrado en profundidad: {limite}\n") #Imprime un mensaje indicando que se encontró la solución en el límite de profundidad actual
                return resultado #Devuelve el resultado de la búsqueda, que es una lista que representa el camino hacia la solución desde el vértice de inicio hasta el vértice objetivo

        print(f"  No se encontró '{meta}' dentro del límite máximo de {limite_max}.") #Imprime un mensaje indicando que no se encontró la solución dentro del límite máximo de profundidad permitido después de intentar con todos los límites de profundidad desde 0 hasta el límite máximo
        return None #Devuelve None para indicar que no se encontró la solución dentro del límite máximo de profundidad permitido después de intentar con todos los límites de profundidad desde 0 hasta el límite máximo


def main(): #Función principal para crear un grafo, agregar vértices y aristas, y realizar búsquedas utilizando el algoritmo IDDFS
    g = Grafica() #Crea una instancia de la clase Grafica para representar el grafo

    for v in [9, 2, 6, 4, 5, 10, 1, 8, 7]: #Agrega vértices al grafo utilizando un bucle para iterar sobre una lista de identificadores de vértices y llamar a la función agregarVertice para cada vértice en la lista
        g.agregarVertice(v) #Agrega un vértice al grafo utilizando la función agregarVertice para cada vértice en la lista de identificadores de vértices

   
    g.agregarArista(9, 2) #Agrega aristas entre los vértices en el grafo utilizando la función agregarArista para establecer conexiones entre los vértices según la estructura del grafo definida por las aristas
    g.agregarArista(9, 6) #Agrega una arista entre el vértice 9 y el vértice 6 en el grafo utilizando la función agregarArista para establecer una conexión entre estos dos vértices
    g.agregarArista(9, 4) #Agrega una arista entre el vértice 9 y el vértice 4 en el grafo utilizando la función agregarArista para establecer una conexión entre estos dos vértices
    g.agregarArista(2, 5) #Agrega una arista entre el vértice 2 y el vértice 5 en el grafo utilizando la función agregarArista para establecer una conexión entre estos dos vértices
    g.agregarArista(6, 10) #Agrega una arista entre el vértice 6 y el vértice 10 en el grafo utilizando la función agregarArista para establecer una conexión entre estos dos vértices
    g.agregarArista(4, 1) #Agrega una arista entre el vértice 4 y el vértice 1 en el grafo utilizando la función agregarArista para establecer una conexión entre estos dos vértices
    g.agregarArista(5, 8) #Agrega una arista entre el vértice 5 y el vértice 8 en el grafo utilizando la función agregarArista para establecer una conexión entre estos dos vértices
    g.agregarArista(1, 7) #Agrega una arista entre el vértice 1 y el vértice 7 en el grafo utilizando la función agregarArista para establecer una conexión entre estos dos vértices

    print("=" * 45) #Imprime una línea de separación para mejorar la legibilidad de la salida en la consola, indicando que se está realizando una nueva búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 8 en el grafo, comenzando desde el vértice 9, y luego realiza la búsqueda y almacena el resultado en la variable resultado.
    print("IDDFS buscando el 8:") #Imprime una línea de separación y un mensaje indicando que se está realizando una búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 8 en el grafo, comenzando desde el vértice 9, y luego realiza la búsqueda y almacena el resultado en la variable resultado.
    resultado = g.IDDFS(9, 8) #Realiza una búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 8 en el grafo, comenzando desde el vértice 9, y luego imprime el camino encontrado hacia el vértice 8.
    print(f"Camino: {resultado}") #Realiza una búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 8 en el grafo, comenzando desde el vértice 9, y luego imprime el camino encontrado hacia el vértice 8.

    print("=" * 45) #Imprime una línea de separación para mejorar la legibilidad de la salida en la consola, indicando que se está realizando una nueva búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 7 en el grafo, comenzando desde el vértice 9, y luego realiza la búsqueda y almacena el resultado en la variable resultado.
    print("IDDFS buscando el 7:")  #Imprime una línea de separación y un mensaje indicando que se está realizando una búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 7 en el grafo, comenzando desde el vértice 9, y luego realiza la búsqueda y almacena el resultado en la variable resultado.0
    resultado = g.IDDFS(9, 7)  #Realiza una búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 7 en el grafo, comenzando desde el vértice 9, y luego imprime el camino encontrado hacia el vértice 7.
    print(f"Camino: {resultado}") #Realiza una búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 7 en el grafo, comenzando desde el vértice 9, y luego imprime el camino encontrado hacia el vértice 7. 

    print("=" * 45) #Imprime una línea de separación para mejorar la legibilidad de la salida en la consola, indicando que se está realizando una nueva búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 10 en el grafo, comenzando desde el vértice 9, y luego realiza la búsqueda y almacena el resultado en la variable resultado.
    print("IDDFS buscando el 10:") #Imprime una línea de separación y un mensaje indicando que se está realizando una búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 10 en el grafo, comenzando desde el vértice 9, y luego realiza la búsqueda y almacena el resultado en la variable resultado.
    resultado = g.IDDFS(9, 10) #Realiza una búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 10 en el grafo, comenzando desde el vértice 9, y luego imprime el camino encontrado hacia el vértice 10.
    print(f"Camino: {resultado}") #Realiza una búsqueda utilizando el algoritmo IDDFS para encontrar el vértice 10 en el grafo, comenzando desde el vértice 9, y luego imprime el camino encontrado hacia el vértice 10.


if __name__ == "__main__": #Verifica si el script se está ejecutando como el programa principal y, si es así, llama a la función
    main()   #Llama a la función principal para ejecutar el programa y realizar las búsquedas utilizando el algoritmo IDDFS en el grafo definido con los vértices y aristas especificados.