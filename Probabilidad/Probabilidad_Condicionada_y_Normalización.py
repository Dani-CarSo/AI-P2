#46
#Probabilidad Condicionada y Normalización

import numpy as np  # importamos numpy para operaciones matemáticas


p_A     = 0.60   # probabilidad de que ocurra el evento A
p_B     = 0.50   # probabilidad de que ocurra el evento B
p_A_y_B = 0.30   # probabilidad de que ocurran A y B al mismo tiempo (intersección)

# dividimos la intersección entre P(B) para "quedarnos solo en el mundo de B"
p_A_dado_B = p_A_y_B / p_B

# dividimos la intersección entre P(A) para "quedarnos solo en el mundo de A"
p_B_dado_A = p_A_y_B / p_A

print("── Probabilidad Condicionada ──")
print(f"P(A|B) = {p_A_dado_B:.4f}")   # muestra el resultado con 4 decimales
print(f"P(B|A) = {p_B_dado_A:.4f}")   # muestra el resultado con 4 decimales

# dos eventos son independientes si P(A∩B) == P(A) * P(B)
# np.isclose compara con tolerancia numérica para evitar errores de redondeo
print(f"¿Independientes? {np.isclose(p_A_y_B, p_A * p_B)}")


# definimos pesos arbitrarios (no tienen por qué sumar 1 todavía)
pesos = np.array([3, 1, 2, 4], dtype=float)  # dtype=float para división exacta

# normalizamos: dividimos cada peso entre la suma total
# así cada valor queda entre 0 y 1, y todos juntos suman exactamente 1
dist = pesos / pesos.sum()

print("\n── Normalización ──")
print(f"Pesos originales : {pesos}")   # vector antes de normalizar
print(f"Distribución     : {dist}")    # vector después de normalizar
print(f"Suma             : {dist.sum():.4f}")  # debe ser 1.0000

# entropía de Shannon: mide cuánta incertidumbre hay en la distribución
# fórmula: H = -Σ p_i * log2(p_i)
# sumamos 1e-12 para evitar log(0) cuando alguna probabilidad es cero
entropia = -np.sum(dist * np.log2(dist + 1e-12))
print(f"Entropía H       : {entropia:.4f} bits")  # a más entropía, más incertidumbre


prevalencia   = 0.05   # P(Enfermo): proporción de enfermos en la población
sensibilidad  = 0.90   # P(+|Enfermo): probabilidad de dar positivo si estás enfermo
especificidad = 0.95   # P(-|Sano): probabilidad de dar negativo si estás sano

# tasa de falsos positivos: probabilidad de dar positivo aunque estés sano
tasa_fp = 1 - especificidad

# P(+): probabilidad total de obtener un positivo (usando la ley de probabilidad total)
# = positivos reales  +  falsos positivos
p_pos = sensibilidad * prevalencia + tasa_fp * (1 - prevalencia)

# P(-): probabilidad total de obtener un negativo (complemento de P(+))
p_neg = 1 - p_pos

# P(Enfermo | Prueba +): aplicamos Bayes
# numerador = P(+|Enfermo) * P(Enfermo)
# denominador = P(+) total
p_enf_dado_pos = (sensibilidad * prevalencia) / p_pos

# P(Enfermo | Prueba -): probabilidad de estar enfermo aunque la prueba salió negativa
# numerador = P(-|Enfermo) * P(Enfermo)  donde P(-|Enfermo) = 1 - sensibilidad
p_enf_dado_neg = ((1 - sensibilidad) * prevalencia) / p_neg

print("\n── Teorema de Bayes (prueba diagnóstica) ──")
print(f"P(Enfermo | Prueba +) = {p_enf_dado_pos:.4f}")  # suele ser más bajo de lo esperado
print(f"P(Enfermo | Prueba −) = {p_enf_dado_neg:.4f}")  # muy bajo si la prueba es buena