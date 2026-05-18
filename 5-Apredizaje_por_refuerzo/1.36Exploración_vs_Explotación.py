#36
#Exploración vs Explotación

import random  # Importa la librería para generar números aleatorios

print(" Exploración vs Explotación ")  # Título del programa

# Valores ocultos (uno será mejor que otro, pero el usuario no lo sabe)
caja_A = random.randint(1, 10)  # Genera un valor aleatorio para la caja A (entre 1 y 10)
caja_B = random.randint(1, 10)  # Genera un valor aleatorio para la caja B (entre 1 y 10)

# Variables para guardar el historial de ganancias
total_A = 0  # Suma total de lo ganado con la caja A
total_B = 0  # Suma total de lo ganado con la caja B
veces_A = 0  # Cuántas veces se ha elegido la caja A
veces_B = 0  # Cuántas veces se ha elegido la caja B

rondas = int(input("¿Cuántas veces quieres jugar?: "))  
# Pide al usuario cuántas rondas quiere jugar y lo convierte a número entero

for i in range(rondas):  # Bucle que se repite según el número de rondas
    print(f"\nRonda {i+1}")  # Muestra el número de la ronda actual

    print("1 = Elegir A")  # Opción para elegir la caja A
    print("2 = Elegir B")  # Opción para elegir la caja B

    eleccion = input("Tu elección: ")  
    # Guarda la opción que el usuario escribe (1 o 2)

    if eleccion == "1":  # Si el usuario eligió la caja A
        recompensa = caja_A + random.randint(-1, 1)  
        # La recompensa es el valor de A más un pequeño ruido aleatorio (-1, 0 o 1)

        total_A += recompensa  # Se suma la recompensa al total de la caja A
        veces_A += 1  # Se incrementa el contador de veces que se eligió A
        print("Elegiste A")  # Mensaje informativo

    else:  # Si el usuario eligió cualquier otra cosa (normalmente "2")
        recompensa = caja_B + random.randint(-1, 1)  
        # Igual que arriba pero con la caja B

        total_B += recompensa  # Se suma la recompensa al total de la caja B
        veces_B += 1  # Se incrementa el contador de veces que se eligió B
        print("Elegiste B")  # Mensaje informativo

    print("Ganaste:", recompensa)  # Muestra cuánto ganó en esa ronda

    # Cálculo de promedios (qué tan buena parece cada caja)
    prom_A = total_A / veces_A if veces_A > 0 else 0  
    # Si ya se usó A, calcula promedio; si no, evita dividir entre 0

    prom_B = total_B / veces_B if veces_B > 0 else 0  
    # Lo mismo para la caja B

    print("Promedio A:", round(prom_A, 2))  
    # Muestra el promedio de A redondeado a 2 decimales

    print("Promedio B:", round(prom_B, 2))  
    # Muestra el promedio de B redondeado

print("\nVALORES REALES (secreto):")  
# Al final revela los valores reales de cada caja

print("Caja A:", caja_A)  # Muestra el valor real de la caja A
print("Caja B:", caja_B)  # Muestra el valor real de la caja B