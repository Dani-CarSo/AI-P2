#32
#Teoría de Juegos: Equilibrios y Mecanismos


print("=== Teoría de Juegos: Equilibrios y Mecanismos ===")  # Imprime el título del programa


estrategias = ["playa", "museo", "aventura"]  # Lista de estrategias disponibles para ambos jugadores


# Diccionario que representa la matriz de pagos del juego
# Cada clave es una tupla (estrategia A, estrategia B)
# Cada valor es otra tupla (pago A, pago B)
pagos_base = {
    ("playa", "playa"): (3, 3),        # Ambos van a playa → saturación moderada
    ("playa", "museo"): (6, 4),        # A gana más, B gana menos
    ("playa", "aventura"): (5, 7),     # B gana más, A gana medio

    ("museo", "playa"): (4, 6),        # Inverso del anterior
    ("museo", "museo"): (5, 5),        # Ambos eligen museo → equilibrio moderado
    ("museo", "aventura"): (3, 8),     # B obtiene mayor beneficio

    ("aventura", "playa"): (7, 5),     # A obtiene mayor beneficio
    ("aventura", "museo"): (8, 3),     # A gana más
    ("aventura", "aventura"): (6, 6)   # Ambos eligen aventura → buena experiencia
}


# Definimos una función que modifica los pagos del juego
# Esto representa un mecanismo de incentivos (por ejemplo, políticas públicas)
def aplicar_mecanismo(pagos):
    
    nuevos_pagos = {}  # Creamos un nuevo diccionario vacío para guardar pagos modificados
    
    # Recorremos cada combinación de estrategias y sus pagos originales
    for (a, b), (pa, pb) in pagos.items():
        
        nuevo_pa = pa  # Copiamos el pago original del jugador A
        nuevo_pb = pb  # Copiamos el pago original del jugador B
        
        # Regla 1: penalizar si ambos eligen playa (para evitar saturación)
        if a == "playa" and b == "playa":
            nuevo_pa -= 2  # Restamos 2 al pago de A
            nuevo_pb -= 2  # Restamos 2 al pago de B
        
        # Regla 2: incentivar diversidad de elecciones
        if a != b:
            nuevo_pa += 1  # Sumamos 1 al pago de A
            nuevo_pb += 1  # Sumamos 1 al pago de B
        
        # Guardamos el nuevo resultado en el diccionario
        nuevos_pagos[(a, b)] = (nuevo_pa, nuevo_pb)
    
    return nuevos_pagos  # Retornamos la nueva matriz de pagos

# Aplicamos el mecanismo a la matriz base
pagos = aplicar_mecanismo(pagos_base)  # Ahora "pagos" contiene los valores modificados


# Pedimos al usuario la estrategia del jugador A
A = input("Jugador A elige (playa/museo/aventura): ").lower()

# Pedimos al usuario la estrategia del jugador B
B = input("Jugador B elige (playa/museo/aventura): ").lower()

# Validamos que las estrategias ingresadas sean correctas
if A in estrategias and B in estrategias:
    print("\nPago con mecanismo:", pagos[(A, B)])  # Mostramos el resultado correspondiente
else:
    print("Entrada inválida ")  # Mensaje de error si la entrada no es válida



print("\nBuscando Equilibrios de Nash ")  # Mensaje de inicio

equilibrios = []  # Lista vacía donde se almacenarán los equilibrios encontrados

# Recorremos todas las combinaciones posibles de estrategias
for a in estrategias:
    for b in estrategias:
        
        pago_actual = pagos[(a, b)]  # Obtenemos el pago actual para la combinación (a, b)
        
        mejor_A = True  # Suponemos inicialmente que es la mejor respuesta
        
        # Probamos todas las posibles desviaciones de A
        for otra_a in estrategias:
            # Si existe otra estrategia que le da mayor pago a A
            if pagos[(otra_a, b)][0] > pago_actual[0]:
                mejor_A = False  # Entonces no es mejor respuesta
        
        
        mejor_B = True  # Suponemos inicialmente que es la mejor respuesta
        
        # Probamos todas las posibles desviaciones de B
        for otra_b in estrategias:
            # Si existe otra estrategia que mejora el pago de B
            if pagos[(a, otra_b)][1] > pago_actual[1]:
                mejor_B = False  # Entonces no es mejor respuesta
    
        
        # Un equilibrio ocurre cuando ambos están jugando mejores respuestas
        if mejor_A and mejor_B:
            equilibrios.append((a, b))  # Guardamos la combinación como equilibrio

# Verificamos si se encontraron equilibrios
if equilibrios:
    print("Equilibrios encontrados:")  # Mensaje
    for eq in equilibrios:
        print("→", eq)  # Mostramos cada equilibrio
else:
    print("No hay equilibrio")  # Caso en que no exista ninguno

print("\nInterpretación:")  # Título
print("El mecanismo modifica los incentivos para cambiar el comportamiento de los jugadores.")  # Explicación
print("El equilibrio de Nash ocurre cuando ningún jugador puede mejorar su pago cambiando solo su estrategia.")  # Definición