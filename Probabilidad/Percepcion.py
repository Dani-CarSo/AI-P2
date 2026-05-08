#44
#Percepcion

# INICIO DEL PROGRAMA
# Muestra el título del programa en pantalla
# ENTRADA DE DATOS
# Simulamos un sensor de distancia

# Pide al usuario la distancia del objeto
# float convierte el dato a número decimal
distancia = float(input("Ingresa la distancia del objeto en metros: "))

# PROCESO DE PERCEPCIÓN
# El sistema interpreta la distancia

# Si la distancia es menor o igual a 2 metros
if distancia <= 2:

    # Muestra que el objeto está muy cerca
    print("Objeto MUY CERCA")

# Si no se cumple lo anterior pero sí es menor o igual a 5
elif distancia <= 5:

    # Muestra que el objeto está cerca
    print("Objeto CERCA")

# Si no se cumple lo anterior pero sí es menor o igual a 10
elif distancia <= 10:

    # Muestra que el objeto está lejos
    print("Objeto LEJOS")

# Si ninguna condición anterior se cumple
else:

    # Significa que no hay objetos cercanos
    print("No se detectan objetos cercanos")

# -----------------------------
# DETECCIÓN EXTRA
# -----------------------------
# Identifica posible peligro

# Si el objeto está a menos de 1 metro
if distancia < 1:

    # Muestra alerta de peligro
    print("¡Water with pennywise")