#13
#Busqueda de Temple Simulado

import math
import random
import time


def distancia(ciudad_a, ciudad_b):
    dx = ciudad_a[0] - ciudad_b[0]
    dy = ciudad_a[1] - ciudad_b[1]
    return math.sqrt(dx * dx + dy * dy)


def distancia_total(tour, ciudades):
    total = 0.0
    n = len(tour)
    for i in range(n):
        total += distancia(ciudades[tour[i]], ciudades[tour[(i + 1) % n]])
    return total


def two_opt(tour):
    n = len(tour)
    i = random.randint(0, n - 2)
    j = random.randint(i + 1, n - 1)
    return tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]


def swap_dos(tour):
    nuevo = tour[:]
    i, j = random.sample(range(len(tour)), 2)
    nuevo[i], nuevo[j] = nuevo[j], nuevo[i]
    return nuevo


def tour_greedy(ciudades):
    n = len(ciudades)
    visitado = [False] * n
    tour = [0]
    visitado[0] = True

    for _ in range(n - 1):
        actual = tour[-1]
        mejor_d = float("inf")
        siguiente = -1
        for j in range(n):
            if not visitado[j]:
                d = distancia(ciudades[actual], ciudades[j])
                if d < mejor_d:
                    mejor_d = d
                    siguiente = j
        tour.append(siguiente)
        visitado[siguiente] = True

    return tour


def simulated_annealing(
    ciudades,
    temperatura_inicial=1.0,
    enfriamiento=0.9995,
    temperatura_minima=1e-4,
    max_iter=None,
    semilla=None,
):
    
    if semilla is not None:
        random.seed(semilla)

    n = len(ciudades)
    tour_actual = tour_greedy(ciudades)
    dist_actual = distancia_total(tour_actual, ciudades)

    mejor_tour = tour_actual[:]
    mejor_dist = dist_actual

    T = temperatura_inicial
    iteracion = 0
    mejoras = 0
    historial = []
    inicio = time.perf_counter()

    while T > temperatura_minima:
        if max_iter and iteracion >= max_iter:
            break

        vecino = two_opt(tour_actual) if random.random() < 0.5 else swap_dos(tour_actual)
        dist_vecino = distancia_total(vecino, ciudades)
        delta = dist_vecino - dist_actual

       
        if delta < 0 or random.random() < math.exp(-delta / T):
            tour_actual = vecino
            dist_actual = dist_vecino
            if dist_actual < mejor_dist:
                mejor_dist = dist_actual
                mejor_tour = tour_actual[:]
                mejoras += 1

        T *= enfriamiento
        iteracion += 1

        if iteracion % 1000 == 0:
            historial.append({
                "iteracion": iteracion,
                "temperatura": round(T, 6),
                "dist_actual": round(dist_actual, 2),
                "mejor_dist":  round(mejor_dist, 2),
            })

    t = time.perf_counter() - inicio
    print(f"Ciudades: {n} | Iters: {iteracion:,} | Mejoras: {mejoras} | "
          f"Mejor dist: {mejor_dist:.2f} | Tiempo: {t:.3f}s")

    return mejor_tour, mejor_dist, historial


if __name__ == "__main__":
    random.seed(42)
    ciudades = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(20)]

    tour, dist, historial = simulated_annealing(ciudades, semilla=42)

    print("\nTour encontrado:")
    for i, idx in enumerate(tour):
        print(f"  {i+1:>2}. Ciudad {idx} → {ciudades[idx]}")