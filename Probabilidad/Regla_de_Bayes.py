#49
#Regla de Bayes

# Pedimos al usuario la probabilidad previa
# Ejemplo: probabilidad de tener una enfermedad
prob_a = float(input("Ingresa P(A) (probabilidad inicial de A): "))

# Pedimos la probabilidad de B dado A
# Ejemplo: probabilidad de dar positivo si sí tiene la enfermedad
prob_b_dado_a = float(input("Ingresa P(B|A): "))

# Pedimos la probabilidad de B
# Ejemplo: probabilidad total de dar positivo
prob_b = float(input("Ingresa P(B): "))

# Aplicamos la fórmula de Bayes
# P(A|B) = (P(B|A) * P(A)) / P(B)
resultado = (prob_b_dado_a * prob_a) / prob_b

# Mostramos el resultado
print("\nResultado usando la Regla de Bayes:")
print("P(A|B) =", round(resultado, 4))