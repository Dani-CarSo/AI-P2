#4
#Busqueda en profundidad limitada

class Vertice: #representa un vértice en el grafo
    def __init__(self, i):  #inicializa el vértice con un identificador, estado de visitado, padre y lista de vecinos
        self.id = i #identificador del vértice
        self.visitado = False #indica si el vértice ha sido visitado durante la búsqueda
        self.padre = None #referencia al vértice padre en la ruta de búsqueda
        self.vecinos = []  #lista de vértices vecinos conectados a este vértice

    def agregarVecino(self, v): #agrega un vértice vecino a la lista de vecinos del vértice actual
        if v not in self.vecinos: #verifica si el vértice vecino ya está en la lista de vecinos para evitar duplicados
            self.vecinos.append(v) #agrega el vértice vecino a la lista de vecinos del vértice actual


class Grafica: #representa un grafo utilizando una estructura de vértices y aristas
    def __init__(self): #inicializa la gráfica con un diccionario vacío para almacenar los vértices
        self.vertices = {}  #diccionario que mapea identificadores de vértices a objetos de la clase Vertice

    def agregarVertice(self, v):  #agrega un vértice al grafo si no existe previamente 
        if v not in self.vertices:  #verifica si el vértice ya existe en el grafo para evitar duplicados
             
            self.vertices[v] = Vertice(v)  #crea un nuevo objeto de la clase Vertice con el identificador dado y lo agrega al diccionario de vértices del grafo

    def agregarArista(self, a, b): #agrega una arista entre dos vértices en el grafo si ambos vértices existen
        if a in self.vertices and b in self.vertices: #verifica si ambos vértices existen en el grafo antes de agregar la arista
            self.vertices[a].agregarVecino(b) #agrega el vértice b como vecino del vértice a
            self.vertices[b].agregarVecino(a)  #agrega el vértice a como vecino del vértice b para mantener la simetría en la representación del grafo

    def resetVisitados(self):   # reinicia el estado de visitado de todos los vértices en el grafo para permitir nuevas búsquedas sin interferencias de estados anteriores
        for v in self.vertices: #itera sobre todos los vértices en el grafo
            self.vertices[v].visitado = False  # marca el vértice como no visitado
            self.vertices[v].padre = None  # reinicia la referencia al padre del vértice para limpiar cualquier ruta de búsqueda anterior

    def DLS(self, nodo, meta, limite, profundidad=0):  #realiza una búsqueda en profundidad limitada (DLS) desde un nodo inicial hasta un nodo meta, con un límite de profundidad especificado
        
        if nodo not in self.vertices:  #verifica si el nodo inicial existe en el grafo antes de comenzar la búsqueda
            print(f"El nodo '{nodo}' no existe en el grafo.") #si el nodo no existe, se imprime un mensaje de error y se retorna None para indicar que la búsqueda no puede continuar
            return None  #retorna None para indicar que la búsqueda no puede continuar debido a la ausencia del nodo inicial en el grafo

        print(f"  Visitando: {nodo} (profundidad {profundidad})")  #imprime el nodo actual que se está visitando junto con su profundidad en la búsqueda para proporcionar información sobre el progreso de la búsqueda
        self.vertices[nodo].visitado = True  #marca el nodo actual como visitado para evitar ciclos y redundancias en la búsqueda

        if nodo == meta:  #verifica si el nodo actual es el nodo meta que se está buscando
            return [nodo]  #si el nodo actual es el nodo meta, se retorna una lista que contiene solo ese nodo, indicando que se ha encontrado la solución

       
        if profundidad >= limite:  #verifica si la profundidad actual de la búsqueda ha alcanzado o superado el límite de profundidad especificado
            print(f"  Límite alcanzado en: {nodo}")  #si se ha alcanzado el límite de profundidad, se imprime un mensaje indicando que el límite ha sido alcanzado en el nodo actual y se retorna None para indicar que no se puede continuar la búsqueda más allá de este punto
            return None  #retorna None para indicar que no se puede continuar la búsqueda más allá del límite de profundidad especificado

       
        for vecino in self.vertices[nodo].vecinos:   #itera sobre los vecinos del nodo actual para continuar la búsqueda en profundidad limitada
            if not self.vertices[vecino].visitado:  #verifica si el vecino actual no ha sido visitado para evitar ciclos y redundancias en la búsqueda
                self.vertices[vecino].padre = nodo  #establece el nodo actual como el padre del vecino para mantener la referencia de la ruta de búsqueda
                resultado = self.DLS(vecino, meta, limite, profundidad + 1)  #realiza una llamada recursiva a la función DLS para continuar la búsqueda desde el vecino actual, incrementando la profundidad en 1

                if resultado is not None:   # verifica si el resultado de la llamada recursiva no es None, lo que indica que se ha encontrado una solución en esa rama de la búsqueda
                    return [nodo] + resultado  #si se ha encontrado una solución, se retorna una lista que combina el nodo actual con el resultado de la búsqueda recursiva, construyendo así la ruta desde el nodo inicial hasta el nodo meta

        return None  #si se han explorado todos los vecinos del nodo actual y no se ha encontrado una solución, se retorna None para indicar que no se ha encontrado la solución en esta rama de la búsqueda


def main():  # función principal que crea un grafo, agrega vértices y aristas, y realiza búsquedas en profundidad limitada (DLS) para demostrar su funcionamiento
    g = Grafica()  #crea una instancia de la clase Grafica para representar el grafo en el que se realizarán las búsquedas

  
    for v in ["A", "B", "C", "D", "E", "F"]: #agrega vértices al grafo utilizando un bucle para iterar sobre una lista de identificadores de vértices y llamar al método agregarVertice para cada uno de ellos
        g.agregarVertice(v)  #agrega cada vértice al grafo utilizando el método agregarVertice de la clase Grafica para construir la estructura del grafo antes de realizar las búsquedas

   
    g.agregarArista("A", "B")   # agrega aristas entre los vértices del grafo utilizando el método agregarArista de la clase Grafica para establecer las conexiones entre los vértices y definir la estructura del grafo antes de realizar las búsquedas
    g.agregarArista("A", "C")   # agrega una arista entre los vértices "A" y "C" para conectar estos dos vértices en el grafo, lo que permite que la búsqueda en profundidad limitada (DLS) pueda explorar esta conexión durante su ejecución
    g.agregarArista("B", "D")   # agrega una arista entre los vértices "B" y "D" para conectar estos dos vértices en el grafo, lo que permite que la búsqueda en profundidad limitada (DLS) pueda explorar esta conexión durante su ejecución
    g.agregarArista("C", "D")   # agrega una arista entre los vértices "C" y "D" para conectar estos dos vértices en el grafo, lo que permite que la búsqueda en profundidad limitada (DLS) pueda explorar esta conexión durante su ejecución
    g.agregarArista("C", "E")   # agrega una arista entre los vértices "C" y "E" para conectar estos dos vértices en el grafo, lo que permite que la búsqueda en profundidad limitada (DLS) pueda explorar esta conexión durante su ejecución
    g.agregarArista("D", "F")   # agrega una arista entre los vértices "D" y "F" para conectar estos dos vértices en el grafo, lo que permite que la búsqueda en profundidad limitada (DLS) pueda explorar esta conexión durante su ejecución
   
    print("=" * 40) # imprime una línea de separación para mejorar la legibilidad de la salida en la consola antes de realizar las búsquedas en profundidad limitada (DLS) y mostrar los resultados de cada búsqueda de manera clara y organizada
    print("DLS buscando 'F' con límite 2:") #imprime un mensaje indicando que se está realizando una búsqueda en profundidad limitada (DLS) para encontrar el nodo "F" desde el nodo "A" con un límite de profundidad de 2, proporcionando contexto sobre la búsqueda que se va a realizar y los parámetros utilizados para la búsqueda
    g.resetVisitados() #reinicia el estado de visitado de los vértices en el grafo antes de realizar una nueva búsqueda en profundidad limitada (DLS) para encontrar el nodo "F" desde el nodo "A" con un límite de profundidad de 2, asegurando que la búsqueda se realice sin interferencias de estados anteriores y mostrando el resultado de la búsqueda, que puede ser la ruta encontrada o None si no se encuentra una solución dentro del límite especificado
    resultado = g.DLS("A", "F", limite=2) #realiza una búsqueda en profundidad limitada (DLS) para encontrar el nodo "F" desde el nodo "A" con un límite de profundidad de 2, mostrando el resultado de la búsqueda, que puede ser la ruta encontrada o None si no se encuentra una solución dentro del límite especificado
    print(f"Resultado: {resultado}")   #imprime el resultado de la búsqueda en profundidad limitada (DLS) para encontrar el nodo "F" desde el nodo "A" con un límite de profundidad de 2, mostrando la ruta encontrada o indicando que no se encontró una solución dentro del límite especificado
    print("=" * 40)  #imprime una línea de separación para mejorar la legibilidad de la salida en la consola antes de realizar la siguiente búsqueda en profundidad limitada (DLS) y mostrar el resultado de esa búsqueda de manera clara y organizada
    print("DLS buscando 'F' con límite 3:") #imprime un mensaje indicando que se está realizando una búsqueda en profundidad limitada (DLS) para encontrar el nodo "F" desde el nodo "A" con un límite de profundidad de 3, proporcionando contexto sobre la búsqueda que se va a realizar y los parámetros utilizados para la búsqueda
    g.resetVisitados()  #reinicia el estado de visitado de los vértices en el grafo antes de realizar una nueva búsqueda en profundidad limitada (DLS) para encontrar el nodo "F" desde el nodo "A" con un límite de profundidad de 3, asegurando que la búsqueda se realice sin interferencias de estados anteriores y mostrando el resultado de la búsqueda, que puede ser la ruta encontrada o None si no se encuentra una solución dentro del límite especificado
    resultado = g.DLS("A", "F", limite=3) #realiza una búsqueda en profundidad limitada (DLS) para encontrar el nodo "F" desde el nodo "A" con un límite de profundidad de 3, mostrando el resultado de la búsqueda, que puede ser la ruta encontrada o None si no se encuentra una solución dentro del límite especificado
    print(f"Resultado: {resultado}")   #imprime el resultado de la búsqueda en profundidad limitada (DLS) para encontrar el nodo "F" desde el nodo "A" con un límite de profundidad de 3, mostrando la ruta encontrada o indicando que no se encontró una solución dentro del límite especificado

    print("=" * 40) #imprime una línea de separación para mejorar la legibilidad de la salida en la consola antes de realizar la siguiente búsqueda en profundidad limitada (DLS) y mostrar el resultado de esa búsqueda de manera clara y organizada
    print("DLS buscando 'E' con límite 2:")  #imprime un mensaje indicando que se está realizando una búsqueda en profundidad limitada (DLS) para encontrar el nodo "E" desde el nodo "A" con un límite de profundidad de 2, proporcionando contexto sobre la búsqueda que se va a realizar y los parámetros utilizados para la búsqueda
    g.resetVisitados()  #reinicia el estado de visitado de los vértices en el grafo antes de realizar una nueva búsqueda en profundidad limitada (DLS) para encontrar el nodo "E" desde el nodo "A" con un límite de profundidad de 2, asegurando que la búsqueda se realice sin interferencias de estados anteriores y mostrando el resultado de la búsqueda, que puede ser la ruta encontrada o None si no se encuentra una solución dentro del límite especificado
    resultado = g.DLS("A", "E", limite=2) #realiza una búsqueda en profundidad limitada (DLS) para encontrar el nodo "E" desde el nodo "A" con un límite de profundidad de 2, mostrando el resultado de la búsqueda, que puede ser la ruta encontrada o None si no se encuentra una solución dentro del límite especificado
    print(f"Resultado: {resultado}")  #imprime el resultado de la búsqueda en profundidad limitada (DLS) para encontrar el nodo "E" desde el nodo "A" con un límite de profundidad de 2, mostrando la ruta encontrada o indicando que no se encontró una solución dentro del límite especificado


if __name__ == "__main__": #verifica si el script se está ejecutando directamente (en lugar de ser importado como un módulo) y, en ese caso, llama a la función main() para iniciar el programa y demostrar el funcionamiento de la búsqueda en profundidad limitada (DLS) en el grafo creado.
    main() #ejecuta la función principal para iniciar el programa y demostrar el funcionamiento de la búsqueda en profundidad limitada (DLS) en el grafo creado.


