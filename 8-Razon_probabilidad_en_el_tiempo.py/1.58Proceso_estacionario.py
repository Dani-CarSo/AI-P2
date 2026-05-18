#58
#Procesos Estacionarios

# Importamos la librería random para generar números aleatorios
import random

# Creamos una lista vacía para guardar los datos
temperaturas = []

# Definimos la media del proceso estacionario
# En un proceso estacionario la media se mantiene estable
media = 25

# Definimos la cantidad de datos a generar
cantidad_datos = 30

# Generamos los datos
for i in range(cantidad_datos):

    # Generamos una variación pequeña alrededor de la media
    variacion = random.randint(-3, 3)

    # Sumamos la variación a la media
    temperatura = media + variacion

    # Guardamos el dato en la lista
    temperaturas.append(temperatura)

# Mostramos los datos generados
print("Datos generados del proceso estacionario:\n")

for i in range(len(temperaturas)):
    print("Día", i + 1, "->", temperaturas[i], "°C")


# Calculamos el promedio del proceso
# Sumamos todos los valores
suma = sum(temperaturas)

# Calculamos el promedio
promedio = suma / len(temperaturas)

# Mostramos el promedio
print("\nPromedio del proceso:", round(promedio, 2))


# Buscamos el valor máximo y mínimo
# Valor máximo
maximo = max(temperaturas)

# Valor mínimo
minimo = min(temperaturas)

# Mostramos resultados
print("Temperatura máxima:", maximo)
print("Temperatura mínima:", minimo)

# Explicación:
# Este proceso es estacionario porque:
# - La media se mantiene cercana a 25
# - Las variaciones son pequeñas
# - No existe una tendencia creciente o decreciente
