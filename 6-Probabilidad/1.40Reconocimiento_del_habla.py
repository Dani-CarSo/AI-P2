#40
#Razonamiento Probabilístico en el Tiempo: Reconocimiento del Habla

# Lista con las palabras que el sistema puede reconocer
palabras = ["hola", "adios", "gracias"]


# Diccionario con probabilidades iniciales
# Cada palabra comienza con una posibilidad similar
probabilidades = {
    "hola": 0.33,
    "adios": 0.33,
    "gracias": 0.34
}


# Mostrar título del programa
print(" Reconocimiento del Habla")


# Explicar qué hará el sistema
print("El sistema intentará reconocer la palabra.")


# Línea vacía para separar texto
print()


# Mostrar las opciones posibles
print("Opciones posibles:")


# Recorrer cada palabra de la lista
for palabra in palabras:

    # Imprimir cada palabra
    print("-", palabra)


# Línea vacía
print()


# Ciclo infinito para escuchar letras continuamente
while True:


    # Pedir al usuario una letra escuchada
    letra = input("Ingresa letra escuchada (o 'fin'): ").lower()


    # Si el usuario escribe "fin"
    if letra == "fin":

        # Terminar el ciclo
        break


    # Recorrer cada palabra posible
    for palabra in palabras:


        # Verificar si la letra está en la palabra
        if letra in palabra:


            # Aumentar probabilidad si coincide
            probabilidades[palabra] += 0.15


        # Si la letra no está
        else:


            # Disminuir probabilidad
            probabilidades[palabra] -= 0.05


        # Evitar valores negativos
        if probabilidades[palabra] < 0:


            # Si es negativa, convertirla en 0
            probabilidades[palabra] = 0


    # Sumar todas las probabilidades
    total = sum(probabilidades.values())


    # Recorrer nuevamente el diccionario
    for palabra in probabilidades:


        # Normalizar probabilidades
        # Esto hace que todas sumen 1
        probabilidades[palabra] = probabilidades[palabra] / total


    # Línea vacía
    print()


    # Mostrar encabezado
    print("Probabilidades actuales:")


    # Recorrer cada palabra y su probabilidad
    for palabra, valor in probabilidades.items():


        # Mostrar porcentaje redondeado
        print(f"{palabra}: {round(valor * 100, 2)}%")


    # Obtener la palabra con mayor probabilidad
    mejor = max(probabilidades, key=probabilidades.get)


    # Línea vacía
    print()


    # Mostrar resultado más probable
    print("El sistema cree que dijiste:", mejor)


    # Línea decorativa
    print("----------------------------------")


# Línea vacía final
print()


# Mensaje de cierre
print("Reconocimiento terminado.")