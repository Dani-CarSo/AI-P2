#26
#Valor de la Información


print(" Decisión Turística Inteligente ")  # Muestra el título del programa

# Pedimos la probabilidad de que el lugar turístico sea bueno
p_bueno = float(input("Probabilidad de que el lugar turístico sea BUENO (0 a 1): "))  # Convertimos a número decimal

# Calculamos la probabilidad de que el lugar sea malo (complemento)
p_malo = 1 - p_bueno  # Si no es bueno, es malo

# Pedimos la ganancia si el lugar resulta ser bueno
ganancia_bueno = float(input("Ganancia si el lugar es bueno: "))  # Ejemplo: 1000

# Pedimos la pérdida si el lugar resulta ser malo
perdida_malo = float(input("Pérdida si el lugar es malo: "))  # Ejemplo: -500

# Pedimos el costo de obtener información (pagar guía turística)
costo_info = float(input("Costo de la guía turística: "))  # Ejemplo: 100

# Calculamos el valor esperado sin información:
# multiplicamos probabilidad de cada caso por su resultado y sumamos
valor_sin_info = (p_bueno * ganancia_bueno) + (p_malo * perdida_malo)


# Si tuvieras información perfecta:
# solo irías cuando el lugar es bueno, y evitarías pérdidas cuando es malo
valor_con_info = (p_bueno * ganancia_bueno) + (p_malo * 0)  # 0 porque no vas si es malo

# Restamos el costo de haber comprado la información
valor_con_info = valor_con_info - costo_info  # pagar la guía reduce el beneficio


# El VOI es la diferencia entre tener información y no tenerla
voi = valor_con_info - valor_sin_info  # cuánto ganas extra por tener información


print("\nRESULTADOS ")  # Salto de línea y título de resultados

# Mostramos el valor esperado sin información
print("Valor esperado SIN información:", valor_sin_info)

# Mostramos el valor esperado con información
print("Valor esperado CON información:", valor_con_info)

# Mostramos el valor de la información
print("Valor de la Información (VOI):", voi)

# Si el VOI es positivo, conviene comprar la información
if voi > 0:  # condición
    print("Conviene comprar la guía turística ")  # mensaje positivo
else:  # si no
    print("NO conviene comprar la guía turística ")  # mensaje negativo
