#15
#Algoritmos Genéticos

import random

# Función objetivo (queremos maximizarla)
def fitness(x): #definir la función objetivo para el algoritmo genético, donde se busca maximizar el valor de la función dada por -(x - 5)**2 + 25, que tiene su máximo en x = 5, lo que representa la mejor solución en el espacio de búsqueda definido por esta función objetivo para el algoritmo genético
    return -(x - 5)**2 + 25  # máximo en x = 5

# Crear individuo (número aleatorio)
def crear_individuo():  #definir una función para crear un individuo en el algoritmo genético, donde se genera un número aleatorio entre -10 y 10 para representar una posible solución en el espacio de búsqueda definido por la función objetivo del algoritmo genético, lo que permite iniciar el proceso evolutivo con una diversidad de soluciones en el espacio de búsqueda
    return random.uniform(-10, 10) #crear un individuo como un número aleatorio entre -10 y 10 para representar una posible solución en el espacio de búsqueda definido por la función objetivo del algoritmo genético

# Crear población inicial
def crear_poblacion(tamano): #definir una función para crear la población inicial del algoritmo genético, donde se genera una lista de individuos utilizando la función crear_individuo() para cada individuo en la población, con un tamaño definido por el parámetro tamano, lo que permite iniciar el proceso evolutivo del algoritmo genético con una diversidad de soluciones en el espacio de búsqueda definido por la función objetivo
    return [crear_individuo() for _ in range(tamano)]   #crear la población inicial con el tamaño definido para comenzar el proceso evolutivo del algoritmo genético, donde cada individuo es un número aleatorio generado por la función crear_individuo() que representa una posible solución en el espacio de búsqueda definido por la función objetivo

# Selección (torneo)
def seleccion(poblacion): #definir una función de selección que implementa el método de torneo para seleccionar un individuo de la población actual, donde se eligen dos individuos al azar y se selecciona el que tenga el valor de fitness más alto para participar en la cruza y generación de un nuevo individuo (hijo) en el proceso evolutivo del algoritmo genético
    a = random.choice(poblacion) #seleccionar dos individuos al azar de la población para el torneo de selección
    b = random.choice(poblacion) #seleccionar dos individuos al azar de la población para el torneo de selección
    return a if fitness(a) > fitness(b) else b  #seleccionar un individuo de la población utilizando el método de torneo, donde se eligen dos individuos al azar y se selecciona el que tenga el valor de fitness más alto para participar en la cruza y generación de un nuevo individuo (hijo) en el proceso evolutivo del algoritmo genético

# Cruza (promedio de padres)
def cruza(padre1, padre2): #definir una función de cruza que combina las características de dos padres seleccionados utilizando un método específico (en este caso, el promedio) para crear un nuevo individuo (hijo) que representa una nueva solución en el espacio de búsqueda del algoritmo genético       
    return (padre1 + padre2) / 2 #combinar las características de dos padres seleccionados utilizando la función de cruza definida para crear un nuevo individuo (hijo) que representa una nueva solución en el espacio de búsqueda del algoritmo genético

# Mutación (pequeña variación)
def mutacion(individuo, prob=0.1): #definir una función de mutación que introduce una pequeña variación aleatoria al individuo con una probabilidad definida para permitir la exploración de nuevas soluciones en el espacio de búsqueda del algoritmo genético
    if random.random() < prob: #con una probabilidad definida, aplicar mutación al individuo para introducir variabilidad en la población y permitir la exploración de nuevas soluciones en el espacio de búsqueda del algoritmo genético
        individuo += random.uniform(-1, 1) #    introducir una pequeña variación aleatoria al individuo con una probabilidad definida para permitir la exploración de nuevas soluciones en el espacio de búsqueda del algoritmo genético       
    return individuo #aplicar mutación al individuo con una probabilidad definida para introducir variabilidad en la población y permitir la exploración de nuevas soluciones en el espacio de búsqueda del algoritmo genético

def algoritmo_genetico(generaciones=20, tamano_poblacion=10): #función principal para ejecutar el algoritmo genético con un número definido de generaciones y tamaño de población para encontrar la mejor solución a través del proceso evolutivo de selección, cruza y mutación en el espacio de búsqueda definido por la función objetivo
    poblacion = crear_poblacion(tamano_poblacion) #crear la población inicial con el tamaño definido para comenzar el proceso evolutivo del algoritmo genético

    for gen in range(generaciones): #iterar por el número de generaciones definido para ejecutar el proceso evolutivo del algoritmo genético a través de selección, cruza y mutación para encontrar la mejor solución en el espacio de búsqueda definido por la función objetivo
        nueva_poblacion = [] #lista para almacenar la nueva población generada a través de selección, cruza y mutación en cada generación del algoritmo genético

        for _ in range(tamano_poblacion): #iterar por el tamaño de la población para generar una nueva población a través de selección, cruza y mutación en cada generación del algoritmo genético
            # Selección
            padre1 = seleccion(poblacion) # seleccionar un padre utilizando la función de selección para elegir un individuo de la población actual para participar en la cruza y generación de un nuevo individuo (hijo) en el proceso evolutivo del algoritmo genético
            padre2 = seleccion(poblacion) # seleccionar un segundo padre utilizando la función de selección para elegir otro individuo de la población actual para participar en la cruza y generación de un nuevo individuo (hijo) en el proceso evolutivo del algoritmo genético 

            # Cruza
            hijo = cruza(padre1, padre2) #generar un nuevo individuo (hijo) a través de la cruza de dos padres seleccionados utilizando la función de cruza definida para combinar las características de los padres y crear una nueva solución en el espacio de búsqueda del algoritmo genético

            # Mutación
            hijo = mutacion(hijo) #aplicar mutación al nuevo individuo generado a través de cruza para introducir variabilidad en la población y permitir la exploración de nuevas soluciones en el espacio de búsqueda del algoritmo genético

            nueva_poblacion.append(hijo)  #agregar el nuevo individuo generado a través de selección, cruza y mutación a la nueva población para construir la siguiente generación en el proceso evolutivo del algoritmo genético

        poblacion = nueva_poblacion  #actualizar la población con la nueva generación de individuos generados a través de selección, cruza y mutación para continuar el proceso evolutivo en el algoritmo genético

        # Mejor individuo de la generación
        mejor = max(poblacion, key=fitness)  #encontrar el mejor individuo de la población actual utilizando la función de fitness para evaluar cada individuo y seleccionar el que tenga el valor más alto como el mejor individuo de la generación
        print(f"Generación {gen+1}: mejor = {mejor}") #imprimir el mejor individuo encontrado en cada generación para mostrar el progreso del algoritmo genético a lo largo de las generaciones

    return max(poblacion, key=fitness) #devolver el mejor individuo encontrado después de completar las generaciones del algoritmo genético para mostrar la mejor solución encontrada al final del proceso de evolución genética

# Ejecutar
resultado = algoritmo_genetico() #ejecutar el algoritmo genético para encontrar la mejor solución después de completar las generaciones definidas en la función del algoritmo genético
print("\nMejor solución encontrada:", resultado) #imprimir la mejor solución encontrada después de completar las generaciones del algoritmo genético
print("Valor de la función:", fitness(resultado)) #imprimir el valor de la función objetivo para la mejor solución encontrada después de completar las generaciones del algoritmo genético