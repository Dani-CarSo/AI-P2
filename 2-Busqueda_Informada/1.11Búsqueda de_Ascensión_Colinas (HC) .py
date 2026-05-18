#11
#Búsqueda de Ascensión de Colinas 

import math #biblioteca para cálculos matemáticos
import random #biblioteca para generar números aleatorios

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

def distancia(coord1, coord2):#función para calcular la distancia entre dos coordenadas utilizando la fórmula de distancia euclidiana
    lat1, lon1 = coord1#desempaquetar las coordenadas de la primera ciudad
    lat2, lon2 = coord2#desempaquetar las coordenadas de la segunda ciudad
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) # calcular la distancia euclidiana entre las dos coordenadas

def evalua_ruta(ruta): #función para evaluar la distancia total de una ruta dada una lista de coordenadas
    total = 0 #inicializar la distancia total a cero
    for i in range(len(ruta) - 1): #iterar a través de la ruta, calculando la distancia entre cada par de ciudades consecutivas
        total += distancia(ruta[i], ruta[i + 1]) #sumar la distancia entre la ciudad actual y la siguiente a la distancia total
    # Cerrar el ciclo: última ciudad → primera 
    total += distancia(ruta[-1], ruta[0]) #sumar la distancia entre la última ciudad y la primera para cerrar el ciclo de la ruta
    return total #devolver la distancia total de la ruta

def i_hill_climbing(): #función para realizar la búsqueda de ascensión de colinas
    # Construir la ruta con las coordenadas (valores del diccionario)
    ruta = list(coord.values()) #crear una lista de las coordenadas de las ciudades a partir de los valores del diccionario
    mejor_ruta = ruta[:] #inicializar la mejor ruta como una copia de la ruta original
    max_iteraciones = 10  #definir el número máximo de iteraciones para la búsqueda de ascensión de colinas

    while max_iteraciones > 0:  #mientras queden iteraciones disponibles
        random.shuffle(ruta)  #mezclar aleatoriamente la ruta para explorar diferentes configuraciones
        mejora = True #inicializar la variable de mejora a True para entrar en el ciclo de búsqueda

        while mejora: #mientras se encuentre una mejora en la ruta
            mejora = False #reiniciar la variable de mejora a False para verificar si se encuentra una mejora en esta iteración
            distancia_actual = evalua_ruta(ruta) #evaluar la distancia total de la ruta actual para compararla con las rutas vecinas

            for i in range(len(ruta) - 1):  #iterar a través de la ruta, considerando cada ciudad como un punto de intercambio para generar rutas vecinas
                if mejora:  #si ya se ha encontrado una mejora, salir del ciclo para evaluar la nueva ruta antes de continuar con más intercambios
                    break  #salir del ciclo de intercambio si se ha encontrado una mejora para evaluar la nueva ruta antes de continuar con más intercambios
                for j in range(len(ruta)): #iterar a través de la ruta nuevamente para generar rutas vecinas intercambiando la ciudad en la posición i con la ciudad en la posición j
                    if i != j: #verificar que no se esté intercambiando la misma ciudad consigo misma
                        ruta_tmp = ruta[:]  #crear una copia temporal de la ruta actual para realizar el intercambio sin modificar la ruta original
                        ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]  #intercambiar las ciudades en las posiciones i y j en la ruta temporal para generar una nueva ruta vecina
                        distancia_tmp = evalua_ruta(ruta_tmp) #evaluar la distancia total de la ruta vecina generada para compararla con la distancia de la ruta actual
                        if distancia_tmp < distancia_actual: #si la distancia de la ruta vecina es menor que la distancia de la ruta actual, se ha encontrado una mejora
                            ruta = ruta_tmp[:] #actualizar la ruta actual con la ruta vecina mejorada para continuar la búsqueda desde esta nueva configuración
                            mejora = True #marcar que se ha encontrado una mejora para continuar buscando mejoras adicionales desde esta nueva ruta
                            break #salir del ciclo de intercambio para evaluar la nueva ruta antes de continuar con más intercambios

        max_iteraciones -= 1 #reducir el número de iteraciones disponibles después de completar una búsqueda de mejoras desde la ruta actual
        if evalua_ruta(ruta) < evalua_ruta(mejor_ruta):  #si la distancia de la ruta actual es menor que la distancia de la mejor ruta encontrada hasta ahora, actualizar la mejor ruta
            mejor_ruta = ruta[:] #actualizar la mejor ruta con la ruta actual si se ha encontrado una mejora significativa en la distancia total

    return mejor_ruta #devolver la mejor ruta encontrada después de completar el número máximo de iteraciones

mejor_ruta = i_hill_climbing()  #ejecutar la función de búsqueda de ascensión de colinas para encontrar la mejor ruta entre las ciudades definidas en el diccionario de coordenadas

# Mostrar nombres de ciudades en lugar de coordenadas
nombres = list(coord.keys()) #crear una lista de los nombres de las ciudades a partir de las claves del diccionario para mostrar los resultados de manera más legible
coordenadas = list(coord.values()) #crear una lista de las coordenadas de las ciudades a partir de los valores del diccionario para facilitar la búsqueda de los nombres correspondientes a las coordenadas en la mejor ruta encontrada

print("Mejor ruta encontrada:")  #imprimir un encabezado para mostrar la mejor ruta encontrada de manera clara
for punto in mejor_ruta:  #iterar a través de las coordenadas en la mejor ruta encontrada para mostrar los nombres de las ciudades correspondientes a cada punto en la ruta
    nombre = nombres[coordenadas.index(punto)] #buscar el nombre de la ciudad correspondiente a las coordenadas del punto actual en la mejor ruta utilizando el índice de las coordenadas en la lista de coordenadas para obtener el nombre de la ciudad desde la lista de nombres
    print(f"  {nombre}: {punto}") #imprimir el nombre de la ciudad y sus coordenadas para cada punto en la mejor ruta encontrada para mostrar los resultados de manera clara y legible

print(f"\nDistancia total: {evalua_ruta(mejor_ruta):.6f}") #imprimir la distancia total de la mejor ruta encontrada utilizando la función de evaluación de ruta para calcular la distancia total y formatear el resultado con seis decimales para mayor precisión en la presentación de los resultados

        
                   