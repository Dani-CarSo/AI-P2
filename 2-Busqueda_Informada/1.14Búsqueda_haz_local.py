#14
#Búsqueda de Haz Local

import random

# Función objetivo (queremos maximizarla)
def objetivo(x):
    return -(x - 5)**2 + 25   # Máximo en x = 5

# Generar vecinos (pequeñas variaciones)
def vecinos(x):  #función para generar vecinos de un estado dado, creando pequeñas variaciones aleatorias alrededor del estado actual para explorar el espacio de soluciones en la búsqueda de haz local
    return [x + random.uniform(-1, 1) for _ in range(5)]   # Genera 5 vecinos con pequeñas variaciones aleatorias

def busqueda_haz_local(k, iteraciones):   #función para realizar la búsqueda de haz local con k estados y un número definido de iteraciones
    # Estados iniciales aleatorios
    estados = [random.uniform(-10, 10) for _ in range(k)] #generar k estados iniciales aleatorios dentro del rango de -10 a 10 para comenzar la búsqueda de haz local

    for i in range(iteraciones): #iterar por el número de iteraciones definido para la búsqueda de haz local
        todos_vecinos = [] #lista para almacenar todos los vecinos generados a partir de los estados actuales en esta iteración de búsqueda de haz local

        # Generar vecinos de todos los estados
        for estado in estados: #iterar a través de los estados actuales para generar vecinos para cada estado utilizando la función de generación de vecinos y agregarlos a la lista de todos los vecinos para evaluar en esta iteración de búsqueda de haz local
            todos_vecinos.extend(vecinos(estado)) #generar vecinos para cada estado actual y agregarlos a la lista de todos los vecinos para evaluar en esta iteración de búsqueda de haz local

        # Seleccionar los k mejores
        estados = sorted(todos_vecinos, key=objetivo, reverse=True)[:k] #ordenar los vecinos por su valor de la función objetivo en orden descendente y seleccionar los k mejores para continuar con la siguiente iteración de búsqueda de haz local

        # Mostrar progreso
        print(f"Iteración {i+1}: mejores estados = {estados}") #imprimir los mejores estados encontrados en cada iteración para mostrar el progreso de la búsqueda de haz local

    # Regresar el mejor estado encontrado
    mejor = max(estados, key=objetivo) #encontrar el estado con el valor máximo de la función objetivo entre los estados finales después de completar las iteraciones de búsqueda de haz local
    return mejor #devolver el mejor estado encontrado después de completar las iteraciones de búsqueda de haz local

# Ejecutar
resultado = busqueda_haz_local(k=3, iteraciones=10) #ejecutar la búsqueda de haz local con 3 estados y 10 iteraciones
print("\nMejor solución encontrada:", resultado) #imprimir la mejor solución encontrada después de completar las iteraciones de búsqueda de haz local
print("Valor de la función:", objetivo(resultado)) #imprimir el valor de la función objetivo para la mejor solución encontrada