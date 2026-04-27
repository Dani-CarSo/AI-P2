#11
#Búsqueda de Ascensión de Colinas 

import math
import random

# Diccionario de ciudades con sus coordenadas
coord = {
    "Guadalajara":        (20.659698, -103.349609),
    "Tepatitlan":         (20.881794, -102.556664),
    "Arandas":            (20.522722, -102.318611),
    "Yahualica":          (21.009722, -102.568611),
    "Mexticacan":         (20.566667, -103.233333),
    "Lagos_de_Moreno":    (21.333333, -102.316667),
    "Jalostotitlan":      (20.483333, -102.816667),
    "Acatic":             (20.483333, -102.566667),
    "San_Juan_de_los_Lagos": (21.083333, -102.316667),
    "Mascota":            (20.516667, -103.366667),
    "Magdalena":          (20.483333, -103.233333),
}

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

def evalua_ruta(ruta):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(ruta[i], ruta[i + 1])
    # Cerrar el ciclo: última ciudad → primera
    total += distancia(ruta[-1], ruta[0])
    return total

def i_hill_climbing():
    # Construir la ruta con las coordenadas (valores del diccionario)
    ruta = list(coord.values())
    mejor_ruta = ruta[:]
    max_iteraciones = 10

    while max_iteraciones > 0:
        random.shuffle(ruta)
        mejora = True

        while mejora:
            mejora = False
            distancia_actual = evalua_ruta(ruta)

            for i in range(len(ruta) - 1):
                if mejora:
                    break
                for j in range(len(ruta)):
                    if i != j:
                        ruta_tmp = ruta[:]
                        ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                        distancia_tmp = evalua_ruta(ruta_tmp)
                        if distancia_tmp < distancia_actual:
                            ruta = ruta_tmp[:]
                            mejora = True
                            break

        max_iteraciones -= 1
        if evalua_ruta(ruta) < evalua_ruta(mejor_ruta):
            mejor_ruta = ruta[:]

    return mejor_ruta

mejor_ruta = i_hill_climbing()

# Mostrar nombres de ciudades en lugar de coordenadas
nombres = list(coord.keys())
coordenadas = list(coord.values())

print("Mejor ruta encontrada:")
for punto in mejor_ruta:
    nombre = nombres[coordenadas.index(punto)]
    print(f"  {nombre}: {punto}")

print(f"\nDistancia total: {evalua_ruta(mejor_ruta):.6f}")

        
                   