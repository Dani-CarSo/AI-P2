#45
#Probabilidad a Priori

# Mostrar un título en pantalla
print("Tráfico ")

# Crear una probabilidad inicial basada en datos históricos
# Aquí se supone que normalmente hay tráfico el 60% de las veces
prob_trafico = 0.60

# Pedir al usuario la hora actual
# int convierte el dato a número entero
hora = int(input("Ingresa la hora actual (0-23): "))

# Preguntar si es día laboral
# lower() convierte el texto a minúsculas
dia_laboral = input("¿Es día laboral? (si/no): ").lower()

# Verificar si la hora está entre 7 y 9 de la mañana
# Estas horas normalmente tienen mucho tráfico
if hora >= 7 and hora <= 9:
    
    # Aumentar la probabilidad de tráfico en 20%
    prob_trafico += 0.20

# Verificar si la hora está entre 6 y 8 de la tarde
# También son horas pico
elif hora >= 18 and hora <= 20:
    
    # Aumentar nuevamente la probabilidad
    prob_trafico += 0.20

# Verificar si NO es día laboral
if dia_laboral == "no":
    
    # Disminuir la probabilidad porque hay menos autos
    prob_trafico -= 0.30

# Mostrar la probabilidad final calculada
print("\nProbabilidad estimada de tráfico:", prob_trafico)

# Si la probabilidad es mayor o igual a 0.80
if prob_trafico >= 0.80:
    
    # Mostrar mensaje de mucho tráfico
    print("Resultado: Es muy probable que haya mucho tráfico.")

# Si la probabilidad es mayor o igual a 0.50
elif prob_trafico >= 0.50:
    
    # Mostrar mensaje de tráfico moderado
    print("Resultado: Podría haber tráfico moderado.")

# Si ninguna condición anterior se cumple
else:
    
    # Mostrar mensaje de poco tráfico
    print("Resultado: Probablemente el camino estará libre.")