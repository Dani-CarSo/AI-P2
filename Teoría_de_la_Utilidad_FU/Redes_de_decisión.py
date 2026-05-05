#25
#Redes de Decisión

print("Transporte Inteligente")
# Muestra un título en pantalla

# Solicitar datos al usuario
distancia = float(input("Ingresa distancia a destino en km: "))
# Pide la distancia y la convierte a número decimal (float)

dinero = float(input("¿Cuánto dinero tienes disponible?: "))
# Pide el dinero disponible y lo convierte a float

trafico = input("¿Hay tráfico? (si/no): ").lower()
# Pide si hay tráfico y convierte la respuesta a minúsculas para evitar errores

# Variables iniciales
opciones = {
    "Carro": 0,
    "Autobus": 0,
    "Bicicleta": 0
}
# Diccionario que guarda las opciones de transporte y su puntuación inicial (0)

# Nodo 1: Distancia
if distancia <= 5:
    opciones["Bicicleta"] += 30
    # Si la distancia es corta, favorece la bicicleta sumando puntos
else:
    opciones["Carro"] += 20
    # Si la distancia es larga, el carro gana puntos
    opciones["Autobus"] += 20
    # También el autobús gana puntos

# Nodo 2: Dinero
if dinero >= 100:
    opciones["Carro"] += 30
    # Si tienes mucho dinero, el carro es mejor opción
elif dinero >= 20:
    opciones["Autobus"] += 25
    # Si tienes dinero moderado, el autobús es buena opción
else:
    opciones["Bicicleta"] += 20
    # Si tienes poco dinero, la bicicleta es mejor

# Nodo 3: Trafico
if trafico == "si":
    opciones["Bicicleta"] += 25
    # Con tráfico, la bicicleta gana ventaja
    opciones["Autobus"] += 15
    # El autobús también gana algo de ventaja
    opciones["Carro"] -= 10
    # El carro pierde puntos por el tráfico
else:
    opciones["Carro"] += 20
    # Sin tráfico, el carro es más conveniente

# Mostrar puntuaciones
print("\nPuntuaciones finales:")
# Imprime título de resultados

for opcion, valor in opciones.items():
    print(opcion, ":", valor)
    # Recorre el diccionario e imprime cada opción con su puntuación

# Mejor decisión
mejor = max(opciones, key=opciones.get)
# Busca la opción con mayor puntuación

print("\nLa mejor decisión es:", mejor)
# Muestra la mejor opción final