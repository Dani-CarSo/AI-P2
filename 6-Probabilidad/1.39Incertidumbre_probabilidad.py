#39
# INCERTIDUMBRE Y PROBABILIDAD

# Mostrar título del programa
print(" Probabilidad de Sacar una Carta Roja ")

# Cantidad de cartas rojas en una baraja
cartas_rojas = 26

# Cantidad de cartas negras en una baraja
cartas_negras = 26

# Total de cartas de la baraja
total_cartas = cartas_rojas + cartas_negras

# Preguntar al usuario cuántas cartas quiere sacar
intentos = int(input("¿Cuántas cartas quieres sacar?: "))

# Variable para contar cuántas cartas rojas salen
rojas_obtenidas = 0

# Ciclo que se repite según la cantidad de intentos
for i in range(intentos):

    # Mostrar número de intento actual
    print("\nCarta número", i + 1)

    # Pedir al usuario el color de la carta obtenida
    carta = input("Escribe el color que salió (roja/negra): ").lower()

    # Verificar si la carta fue roja
    if carta == "roja":

        # Sumar 1 al contador de cartas rojas
        rojas_obtenidas += 1

# Calcular la probabilidad experimental
probabilidad = rojas_obtenidas / intentos

# Convertir la probabilidad a porcentaje
porcentaje = probabilidad * 100

# Mostrar sección de resultados
print("\n RESULTADOS ")

# Mostrar cuántas cartas rojas se obtuvieron
print("Cartas rojas obtenidas:", rojas_obtenidas)

# Mostrar cantidad total de intentos
print("Intentos totales:", intentos)

# Mostrar probabilidad experimental
print("Probabilidad experimental:", probabilidad)

# Mostrar porcentaje
print("Porcentaje:", porcentaje, "%")

# Verificar si la probabilidad es alta
if probabilidad > 0.5:

    # Mensaje si la probabilidad es alta
    print("La probabilidad de obtener roja es alta.")

    # Menor incertidumbre
    print("La incertidumbre es menor.")

# Verificar si la probabilidad es exactamente 0.5
elif probabilidad == 0.5:

    # Mensaje de equilibrio
    print("La probabilidad es equilibrada.")

    # Incertidumbre media
    print("Existe incertidumbre media.")

# Si la probabilidad es menor a 0.5
else:

    # Mensaje de baja probabilidad
    print("La probabilidad de obtener roja es baja.")

    # Mayor incertidumbre
    print("La incertidumbre es alta.")

# Calcular probabilidad teórica real
prob_teorica = cartas_rojas / total_cartas

# Mostrar probabilidad teórica
print("\nProbabilidad teórica real de una carta roja:", prob_teorica)

# Mostrar mensaje final
print("\nFin del programa.")