#60
# FILTRADO, PREDICCIÓN, SUAVIZADO Y EXPLICACIÓN

# Lista de temperaturas registradas
datos = [20, 21, 22, 40, 23, 24, 25]

# FILTRADO
# Eliminamos valores demasiado altos
# Lista donde guardaremos los datos filtrados
filtrados = []

# Recorremos cada dato
for valor in datos:

    # Si el valor es menor o igual a 30 lo guardamos
    if valor <= 30:
        filtrados.append(valor)

# Mostramos los datos filtrados
print("Datos filtrados:")
print(filtrados)


# PREDICCIÓN
# Calculamos una predicción usando el promedio
# Sumamos los valores filtrados
suma = sum(filtrados)

# Calculamos el promedio
promedio = suma / len(filtrados)

# Predicción del siguiente valor
prediccion = promedio

# Mostramos la predicción
print("\nPredicción del siguiente dato:")
print(round(prediccion, 2))


# SUAVIZADO
# Promedio móvil para suavizar cambios bruscos
# Lista para guardar resultados suavizados
suavizados = []

# Recorremos desde el segundo elemento
for i in range(1, len(filtrados)):

    # Promedio entre dos valores consecutivos
    promedio_local = (filtrados[i - 1] + filtrados[i]) / 2

    # Guardamos el resultado
    suavizados.append(promedio_local)

# Mostramos resultados suavizados
print("\nDatos suavizados:")
print(suavizados)


# EXPLICACIÓN
# Buscamos por qué hubo un valor extraño
# Recorremos los datos originales
for valor in datos:

    # Detectamos valores muy altos
    if valor > 30:

        # Mostramos posible explicación
        print("\nValor extraño detectado:", valor)
        print("Posible explicación: error del sensor o calor extremo")

