#3
#Deep First Search
#Busqueda en Profundidad

class Vertice:
    def __init__(self, i):          
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.padre = None
        self.vecinos = []           

    def agregarVecino(self, v):    
        if v not in self.vecinos:
            self.vecinos.append(v)


class Grafica:
    def __init__(self):           
        self.vertices = {}          

    def agregarVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b)
            self.vertices[b].agregarVecino(a)

    def DFS(self, r):
        if r in self.vertices:
            self.vertices[r].visitado = True
            for nodo in self.vertices[r].vecinos:
                if self.vertices[nodo].visitado == False:
                    self.vertices[nodo].padre = r
                    print("(" + str(nodo) + "," + str(r) + ")")
                    self.DFS(nodo)


def main():
    g = Grafica()
    g.agregarVertice("A")
    g.agregarVertice("B")
    g.agregarVertice("C")
    g.agregarVertice("D")
    g.agregarVertice("E")
    g.agregarArista("A", "B")
    g.agregarArista("A", "C")
    g.agregarArista("B", "D")
    g.agregarArista("C", "D")
    g.agregarArista("C", "E")

    print("DFS:")
    g.DFS("A")


if __name__ == "__main__":
    main()                              
