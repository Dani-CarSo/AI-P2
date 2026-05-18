#51
#Regla de la cadena

# Pedimos la primera probabilidad
# Ejemplo: probabilidad de estudiar
p_a = float(input("Ingresa P(A): "))

# Pedimos la segunda probabilidad condicionada
# Ejemplo: probabilidad de aprobar si estudió
p_b_dado_a = float(input("Ingresa P(B|A): "))

# Aplicamos la Regla de la Cadena
# P(A y B) = P(A) * P(B|A)
resultado = p_a * p_b_dado_a

# Mostramos el resultado
print("\nResultado:")
print("P(A y B) =", round(resultado, 4))