#23
#Acondicionamiento del corte

def cutting_stock(stock_length, piezas): #

    # Ordena la lista de piezas de mayor a menor para aplicar FFD
    # Ejemplo: [2,3,5,4,6,2] → [6,5,4,3,2,2]
    piezas = sorted(piezas, reverse=True)

    # Lista vacía que irá guardando las barras con sus piezas asignadas
    barras = []

    # Recorre cada pieza una por una en el orden ya ordenado
    for pieza in piezas:

        # Bandera que indica si la pieza ya fue colocada en alguna barra
        colocado = False

        # Revisa cada barra que ya existe para ver si la pieza cabe
        for barra in barras:

            # Suma lo que ya ocupa la barra y le agrega el tamaño de la pieza actual
            # Si el resultado no supera la longitud máxima, la pieza sí cabe
            if sum(barra) + pieza <= stock_length:

                # Agrega la pieza a esta barra porque hay espacio suficiente
                barra.append(pieza)

                # Marca que la pieza ya fue colocada y sale del for de barras
                colocado = True
                break

        # Si después de revisar todas las barras la pieza no cupo en ninguna
        if not colocado:

            # Crea una nueva barra con solo esta pieza adentro
            barras.append([pieza])

    # Devuelve la lista completa de barras con sus piezas asignadas
    return barras

#Datos de entrada 
# Longitud estándar de cada barra de material disponible
stock_length = 10
# Lista de piezas que se necesitan cortar (en las mismas unidades)
piezas = [2, 3, 5, 4, 6, 2]
# Ejecutar el algoritmo
# Llama a la función y guarda el resultado en una variable
resultado = cutting_stock(stock_length, piezas)


# Mostrar resultado 
print("Cortes realizados:")

# Recorre cada barra junto con su índice (enumerate empieza en 1)
for i, barra in enumerate(resultado):

    # Imprime el número de barra, las piezas que contiene y cuánto suman
    print(f"Barra {i+1}: {barra} → total = {sum(barra)}")