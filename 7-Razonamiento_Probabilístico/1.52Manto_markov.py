#52
#Manto Markov

# Creamos un diccionario llamado "red"
# Aquí guardamos las conexiones entre nodos
red = {

    # El nodo "Clima" tiene conexión con
    # "Lluvia" y "Temperatura"
    "Clima": ["Lluvia", "Temperatura"],

    # El nodo "Lluvia" se conecta con
    # "Paraguas" y "Tráfico"
    "Lluvia": ["Paraguas", "Tráfico"],

    # El nodo "Temperatura" se conecta con
    # "Aire acondicionado"
    "Temperatura": ["Aire acondicionado"],

    # Estos nodos no tienen hijos
    "Paraguas": [],
    "Tráfico": [],
    "Aire acondicionado": []
}

# Pedimos al usuario escribir un nodo
nodo = input("Ingresa el nombre del nodo: ")

# Verificamos si el nodo existe en la red
if nodo in red:

    # Guardamos los hijos del nodo seleccionado
    hijos = red[nodo]

    # Creamos una lista vacía para los padres
    padres = []

    # Recorremos cada nodo de la red
    for clave in red:

        # Revisamos si el nodo seleccionado
        # aparece dentro de las conexiones
        if nodo in red[clave]:

            # Si aparece, significa que "clave"
            # es padre del nodo
            padres.append(clave)

    # Mostramos el nodo seleccionado
    print("\nNodo seleccionado:", nodo)

    # Mostramos los padres encontrados
    print("Padres:", padres)

    # Mostramos los hijos encontrados
    print("Hijos:", hijos)

    # El Manto de Markov se forma con
    # padres + hijos
    manto = padres + hijos

    # Mostramos el Manto de Markov
    print("Manto de Markov:", manto)

# Si el nodo no existe
else:

    # Mostramos mensaje de error
    print("El nodo no existe en la red.")