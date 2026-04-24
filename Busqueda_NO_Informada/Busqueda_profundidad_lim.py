#4
#Busque en profundidad limitada

class Vertice:
    def __init__(self, i):
        self.id = i
        self.visitado = False
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

    def resetVisitados(self):
        """Reinicia el estado visitado de todos los vértices."""
        for v in self.vertices:
            self.vertices[v].visitado = False
            self.vertices[v].padre = None

    def DLS(self, nodo, meta, limite, profundidad=0):
        
        if nodo not in self.vertices:
            print(f"El nodo '{nodo}' no existe en el grafo.")
            return None

        print(f"  Visitando: {nodo} (profundidad {profundidad})")
        self.vertices[nodo].visitado = True

        if nodo == meta:
            return [nodo]

       
        if profundidad >= limite:
            print(f"  Límite alcanzado en: {nodo}")
            return None

       
        for vecino in self.vertices[nodo].vecinos:
            if not self.vertices[vecino].visitado:
                self.vertices[vecino].padre = nodo
                resultado = self.DLS(vecino, meta, limite, profundidad + 1)

                if resultado is not None:
                    return [nodo] + resultado  

        return None  


def main():
    g = Grafica()

  
    for v in ["A", "B", "C", "D", "E", "F"]:
        g.agregarVertice(v)

   
    g.agregarArista("A", "B")
    g.agregarArista("A", "C")
    g.agregarArista("B", "D")
    g.agregarArista("C", "D")
    g.agregarArista("C", "E")
    g.agregarArista("D", "F")

   

    print("=" * 40)
    print("DLS buscando 'F' con límite 2:")
    g.resetVisitados()
    resultado = g.DLS("A", "F", limite=2)
    print(f"Resultado: {resultado}")   
    print("=" * 40)
    print("DLS buscando 'F' con límite 3:")
    g.resetVisitados()
    resultado = g.DLS("A", "F", limite=3)
    print(f"Resultado: {resultado}")   

    print("=" * 40)
    print("DLS buscando 'E' con límite 2:")
    g.resetVisitados()
    resultado = g.DLS("A", "E", limite=2)
    print(f"Resultado: {resultado}")  


if __name__ == "__main__":
    main()


