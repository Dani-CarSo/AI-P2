#5
#Iterative Deepening Depth-First Search (IDDFS)
#Busqueda en Profundidad Iterativa 

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
        for v in self.vertices:
            self.vertices[v].visitado = False
            self.vertices[v].padre = None

    def DLS(self, nodo, meta, limite, profundidad=0):
        self.vertices[nodo].visitado = True

        if nodo == meta:
            return [nodo]

        if profundidad >= limite:
            return None

        for vecino in self.vertices[nodo].vecinos:
            if not self.vertices[vecino].visitado:
                self.vertices[vecino].padre = nodo
                resultado = self.DLS(vecino, meta, limite, profundidad + 1)
                if resultado is not None:
                    return [nodo] + resultado

        return None

    def IDDFS(self, inicio, meta, limite_max=10):
        if inicio not in self.vertices or meta not in self.vertices:
            print(f"Error: nodo no existe en el grafo.")
            return None

        if inicio == meta:
            return [inicio]

        for limite in range(limite_max + 1):
            print(f"  Intentando con límite de profundidad: {limite}")
            self.resetVisitados()

            resultado = self.DLS(inicio, meta, limite)

            if resultado is not None:
                print(f"  ✅ Encontrado en profundidad: {limite}\n")
                return resultado

        print(f"  No se encontró '{meta}' dentro del límite máximo de {limite_max}.")
        return None


def main():
    g = Grafica()

    for v in [9, 2, 6, 4, 5, 10, 1, 8, 7]:
        g.agregarVertice(v)

   
    g.agregarArista(9, 2)
    g.agregarArista(9, 6)
    g.agregarArista(9, 4)
    g.agregarArista(2, 5)
    g.agregarArista(6, 10)
    g.agregarArista(4, 1)
    g.agregarArista(5, 8)
    g.agregarArista(1, 7)

    print("=" * 45)
    print("IDDFS buscando el 8:")
    resultado = g.IDDFS(9, 8)
    print(f"Camino: {resultado}")

    print("=" * 45)
    print("IDDFS buscando el 7:")
    resultado = g.IDDFS(9, 7)
    print(f"Camino: {resultado}")

    print("=" * 45)
    print("IDDFS buscando el 10:")
    resultado = g.IDDFS(9, 10)
    print(f"Camino: {resultado}")


if __name__ == "__main__":
    main()