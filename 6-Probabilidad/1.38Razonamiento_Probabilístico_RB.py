#38
#Razonamiento Probabilístico: Red Bayesiana

# Mostrar el título principal del programa
print("Probabilidad de Enfermedad ")

# Probabilidad inicial de enfermedad
# Se considera una probabilidad base del 10%
prob_enfermedad = 0.10

# Preguntar al usuario si el paciente tiene fiebre
# .lower() convierte el texto a minúsculas
fiebre = input("¿El paciente tiene fiebre? (si/no): ").lower()

# Preguntar si el paciente tiene tos
tos = input("¿El paciente tiene tos? (si/no): ").lower()

# Preguntar si el paciente tiene cansancio
cansancio = input("¿El paciente tiene cansancio? (si/no): ").lower()

# Verificar si el usuario respondió "si" para fiebre
if fiebre == "si":

    # Aumentar la probabilidad en 35%
    prob_enfermedad += 0.35

# Verificar si el paciente tiene tos
if tos == "si":

    # Aumentar la probabilidad en 25%
    prob_enfermedad += 0.25

# Verificar si el paciente tiene cansancio
if cansancio == "si":

    # Aumentar la probabilidad en 20%
    prob_enfermedad += 0.20

# Verificar que la probabilidad no sea mayor a 1
if prob_enfermedad > 1:

    # Ajustar el valor máximo permitido
    prob_enfermedad = 1

# Convertir la probabilidad a porcentaje
porcentaje = prob_enfermedad * 100

# Mostrar una línea de separación
print("\nRESULTADO DEL ANÁLISIS ")

# Mostrar la probabilidad final calculada
print("Probabilidad de enfermedad:", prob_enfermedad)

# Mostrar el porcentaje final
print("Porcentaje:", porcentaje, "%")

# Verificar si la probabilidad es alta
if prob_enfermedad >= 0.70:

    # Mostrar mensaje de alta probabilidad
    print("Diagnóstico probable.")

# Verificar si la probabilidad es media
elif prob_enfermedad >= 0.40:

    # Mostrar mensaje de incertidumbre moderada
    print("Existe incertidumbre moderada.")

# Si la probabilidad es baja
else:

    # Mostrar mensaje de baja probabilidad
    print("La enfermedad es poco probable.")

# Mostrar mensaje final
print("\nFin del sistema bayesiano.")