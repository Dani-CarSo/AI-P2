#77
#Mapas Autoorganizados de Kohonen


# Importamos random para generar números aleatorios
import random

# ============================================================
# CREACIÓN DE NEURONAS
# ============================================================

# Creamos lista de neuronas
# Cada neurona tendrá dos pesos
neuronas = [

    # Primera neurona con pesos aleatorios
    [random.uniform(0, 1), random.uniform(0, 1)],

    # Segunda neurona con pesos aleatorios
    [random.uniform(0, 1), random.uniform(0, 1)],

    # Tercera neurona con pesos aleatorios
    [random.uniform(0, 1), random.uniform(0, 1)]
]

# ============================================================
# TASA DE APRENDIZAJE
# ============================================================

# Valor que controla cuánto aprenden las neuronas
learning_rate = 0.3


# ============================================================
# MOSTRAMOS INFORMACIÓN INICIAL
# ============================================================

# Mostramos título
print(" MAPAS AUTOORGANIZADOS DE KOHONEN ")

# Mostramos neuronas iniciales
print("\nNeuronas iniciales:")

# Mostramos lista de neuronas
print(neuronas)


# ============================================================
# CICLO PRINCIPAL
# ============================================================

# Creamos ciclo infinito
while True:

    # --------------------------------------------------------
    # PEDIMOS DATOS AL USUARIO
    # --------------------------------------------------------

    # Pedimos primer valor
    x1 = float(input("\nIngresa valor x1: "))

    # Pedimos segundo valor
    x2 = float(input("Ingresa valor x2: "))


    # --------------------------------------------------------
    # BUSCAMOS LA MEJOR NEURONA
    # --------------------------------------------------------

    # Creamos lista vacía para guardar distancias
    distancias = []

    # Recorremos cada neurona
    for neurona in neuronas:

        # Calculamos diferencia en x1
        dx = x1 - neurona[0]

        # Calculamos diferencia en x2
        dy = x2 - neurona[1]

        # Calculamos distancia euclidiana
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        # Guardamos distancia en lista
        distancias.append(distancia)


    # --------------------------------------------------------
    # ENCONTRAMOS LA NEURONA GANADORA
    # --------------------------------------------------------

    # Buscamos la menor distancia
    menor_distancia = min(distancias)

    # Obtenemos posición de la mejor neurona
    ganadora = distancias.index(menor_distancia)


    # --------------------------------------------------------
    # MOSTRAMOS RESULTADO
    # --------------------------------------------------------

    # Mostramos neurona ganadora
    print("\nNeurona ganadora:", ganadora)

    # Mostramos distancia mínima
    print("Distancia mínima:", menor_distancia)


    # --------------------------------------------------------
    # ACTUALIZAMOS PESOS
    # --------------------------------------------------------

    # Ajustamos peso 1 de la neurona ganadora
    neuronas[ganadora][0] = neuronas[ganadora][0] + (
        learning_rate * (x1 - neuronas[ganadora][0])
    )

    # Ajustamos peso 2 de la neurona ganadora
    neuronas[ganadora][1] = neuronas[ganadora][1] + (
        learning_rate * (x2 - neuronas[ganadora][1])
    )


    # --------------------------------------------------------
    # MOSTRAMOS NUEVAS NEURONAS
    # --------------------------------------------------------

    # Mostramos mensaje
    print("\nNeuronas actualizadas:")

    # Mostramos neuronas
    print(neuronas)


    # --------------------------------------------------------
    # EXPLICACIÓN
    # --------------------------------------------------------

    # Mostramos mensaje explicativo
    print("\nLa neurona ganadora se acercó al dato ingresado.")


    # --------------------------------------------------------
    # PREGUNTAMOS SI QUIERE CONTINUAR
    # --------------------------------------------------------

    # Guardamos respuesta
    continuar = input("\n¿Quieres probar otro dato? (si/no): ")


    # --------------------------------------------------------
    # VERIFICAMOS SI QUIERE SALIR
    # --------------------------------------------------------

    # Verificamos respuesta
    if continuar.lower() == "no":

        # Mostramos mensaje final
        print("\nPrograma terminado.")

        # Terminamos ciclo
        break