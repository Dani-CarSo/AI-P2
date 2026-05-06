#37
#Búsqueda de la Política

import random  # Importa la librería para usar números aleatorios (aunque aquí casi no se usa)

print(" Búsqueda de la Política ")  # Muestra el título del programa

meta = 3  # Define el estado final (la meta es llegar al estado 3)

# Función que evalúa una política (una lista de acciones)
def evaluar_politica(politica):
    estado = 0  # Siempre empezamos en el estado 0 (inicio)
    pasos = 0   # Contador de pasos que damos

    print("\nSimulación:")  # Mensaje para mostrar cómo se ejecuta la política

    # Se ejecuta hasta llegar a la meta o máximo 10 pasos
    while estado != meta and pasos < 10:
        accion = politica[estado]  
        # Toma la acción que la política indica para el estado actual

        print(f"Estado: {estado} → Acción: {accion}")  
        # Muestra en qué estado estamos y qué acción se tomó

        if accion == "derecha":
            estado += 1  # Si la acción es derecha, avanzamos
        else:
            estado -= 1  # Si no (izquierda), retrocedemos

        # Evita salir del rango permitido (0 a meta)
        estado = max(0, min(estado, meta))

        pasos += 1  # Aumenta el contador de pasos

    # Si llegó a la meta
    if estado == meta:
        print("Llegaste a la META ")  # Mensaje de éxito
        return 10 - pasos  # Entre menos pasos, mayor puntaje
    else:
        print("No llegaste ")  # Mensaje de fallo
        return -5  # Penalización

# Variables para guardar la mejor política encontrada
mejor_politica = None  # Aquí se guardará la mejor política
mejor_puntaje = -999   # Valor inicial muy bajo para comparar

intentos = int(input("¿Cuántas políticas quieres probar?: "))  
# Pide al usuario cuántas políticas quiere probar

# Bucle principal para probar varias políticas
for i in range(intentos):
    print(f"\n--- Política {i+1} ---")  # Muestra el número de intento

    politica = []  # Lista vacía donde se guardarán las acciones

    # El usuario define qué hacer en cada estado
    for estado in range(4):  # Estados 0,1,2,3
        accion = input(f"Estado {estado} (izquierda/derecha): ").lower()  
        # Pide la acción y la convierte a minúsculas

        politica.append(accion)  
        # Guarda la acción en la política

    puntaje = evaluar_politica(politica)  
    # Evalúa la política creada

    print("Puntaje:", puntaje)  # Muestra el resultado

    # Verifica si es la mejor política hasta ahora
    if puntaje > mejor_puntaje:
        mejor_puntaje = puntaje  # Actualiza el mejor puntaje
        mejor_politica = politica  # Guarda la mejor política

# Mostrar la mejor política encontrada
print("Política:", mejor_politica)  # Muestra la mejor estrategia
print("Puntaje:", mejor_puntaje)   # Muestra su puntaje