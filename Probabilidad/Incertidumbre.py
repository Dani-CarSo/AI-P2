#44
#Incertidumbre

# Pedir al usuario la temperatura actual
temperatura = float(input("Ingresa la temperatura actual: "))

# Si la temperatura es menor o igual a 15
# el sistema considera que hace frío
if temperatura <= 15:
    print("El clima es FRIO")
    
# Si la temperatura es mayor a 15
# y menor a 25, el clima es templado
elif temperatura > 15 and temperatura < 25:
    print("El clima es TEMPLADO")

# Si no se cumplen las condiciones anteriores
# entonces el clima se considera caliente
else:
    print("El clima es CALIENTE")

# Esta condición detecta incertidumbre
# porque la temperatura está justo
# en el límite entre dos categorías
if temperatura == 15 or temperatura == 25:
    print("Existe incertidumbre porque está en el límite entre categorías.")