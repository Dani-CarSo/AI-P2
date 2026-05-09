#48
#Independencia Condicional

import numpy as np                       # Importa NumPy para generar números aleatorios y hacer cálculos
import matplotlib.pyplot as plt          # Importa Matplotlib para crear las gráficas de barras

np.random.seed(7)                        # Fija la semilla aleatoria: garantiza que siempre salgan los mismos números

N = 10_000                               # Define cuántos partidos vamos a simular (10,000 observaciones)

#  Simular C — ¿El jugador entrenó duro esta semana?
C = np.random.binomial(1, 0.5, N)       # Genera N valores de 0 o 1: 1=entrenó duro (50%), 0=no entrenó (50%)


# Simular A y B en función de C

prob_A = np.where(C == 1, 0.75, 0.20)   # Si C=1 (entrenó): prob. de anotar = 75% | Si C=0: prob. = 20%
A      = np.random.binomial(1, prob_A)  # Genera 1 (anotó) o 0 (no anotó) para cada partido según prob_A

prob_B = np.where(C == 1, 0.80, 0.25)  # Si C=1 (entrenó): prob. de correr 10km = 80% | Si C=0: prob. = 25%
B      = np.random.binomial(1, prob_B)  # Genera 1 (corrió) o 0 (no corrió) para cada partido según prob_B


#  Dependencia MARGINAL — sin saber si entrenó
# Si ignoramos C, A y B parecen relacionados (ambas dependen de C)

p_A  = A.mean()                          # P(A=1): proporción de partidos donde anotó (promedio del arreglo A)
p_B  = B.mean()                          # P(B=1): proporción de partidos donde corrió más de 10 km
p_AB = (A & B).mean()                    # P(A=1 y B=1): partidos donde anotó Y corrió al mismo tiempo (AND lógico)

print("=" * 52)                          # Imprime una línea decorativa de separación
print("   SIN CONOCER C (dependencia marginal)")  # Encabezado de la sección
print("=" * 52)                          # Otra línea decorativa
print(f"  P(Anotó)                     = {p_A:.3f}")        # Muestra probabilidad de anotar con 3 decimales
print(f"  P(Corrió 10km)               = {p_B:.3f}")        # Muestra probabilidad de correr con 3 decimales
print(f"  P(Anotó y Corrió)            = {p_AB:.3f}")       # Muestra probabilidad conjunta real
print(f"  P(Anotó) × P(Corrió)         = {p_A * p_B:.3f}") # Calcula qué sería si fueran independientes

diferencia_marginal = abs(p_AB - p_A * p_B)  # Resta entre valor real y valor esperado bajo independencia
print(f"  Diferencia                   = {diferencia_marginal:.3f}  <- mayor que 0 = DEPENDIENTES")


# Independencia CONDICIONAL — sabiendo si entrenó
# Al conocer C, la relación entre A y B desaparece
# Caso C = 1: partidos donde SÍ entrenó duro

idx_C1  = (C == 1)                       # Crea una máscara booleana: True donde C es igual a 1
p_A_C1  = A[idx_C1].mean()              # P(A=1 | C=1): prob. de anotar SOLO en partidos donde entrenó
p_B_C1  = B[idx_C1].mean()              # P(B=1 | C=1): prob. de correr SOLO en partidos donde entrenó
p_AB_C1 = (A[idx_C1] & B[idx_C1]).mean() # P(A=1,B=1 | C=1): ambas cosas juntas cuando sí entrenó

print("\n" + "=" * 52)                   # Salto de línea y separador visual
print("   DADO C=1 (si entrenó duro)")  # Encabezado de esta subsección
print("=" * 52)                          # Línea decorativa
print(f"  P(Anotó | entrenó)           = {p_A_C1:.3f}")             # Prob. de anotar dado que entrenó
print(f"  P(Corrió | entrenó)          = {p_B_C1:.3f}")             # Prob. de correr dado que entrenó
print(f"  P(Anotó y Corrió | entrenó)  = {p_AB_C1:.3f}")            # Prob. conjunta real dado C=1
print(f"  P(Anotó|C) x P(Corrió|C)    = {p_A_C1 * p_B_C1:.3f}")   # Producto si fueran independientes dado C=1

diferencia_C1 = abs(p_AB_C1 - p_A_C1 * p_B_C1)   # Diferencia: si es ~0, son condicionalmente independientes
print(f"  Diferencia                   = {diferencia_C1:.3f}  <- cercana a 0 = INDEPENDIENTES")

#  Caso C = 0: partidos donde NO entrenó duro 

idx_C0  = (C == 0)                       # Máscara booleana: True donde C es igual a 0
p_A_C0  = A[idx_C0].mean()              # P(A=1 | C=0): prob. de anotar SOLO en partidos sin entrenamiento
p_B_C0  = B[idx_C0].mean()              # P(B=1 | C=0): prob. de correr SOLO en partidos sin entrenamiento
p_AB_C0 = (A[idx_C0] & B[idx_C0]).mean() # P(A=1,B=1 | C=0): ambas cosas cuando no entrenó

print("\n" + "=" * 52)                   # Salto de línea y separador
print("   DADO C=0 (no entrenó duro)")  # Encabezado de esta subsección
print("=" * 52)                          # Línea decorativa
print(f"  P(Anotó | no entrenó)        = {p_A_C0:.3f}")             # Prob. de anotar sin haber entrenado
print(f"  P(Corrió | no entrenó)       = {p_B_C0:.3f}")             # Prob. de correr sin haber entrenado
print(f"  P(Anotó y Corrió | no entr.) = {p_AB_C0:.3f}")            # Prob. conjunta real dado C=0
print(f"  P(Anotó|C) x P(Corrió|C)    = {p_A_C0 * p_B_C0:.3f}")   # Producto si fueran independientes dado C=0

diferencia_C0 = abs(p_AB_C0 - p_A_C0 * p_B_C0)   # Diferencia: también debería ser ~0
print(f"  Diferencia                   = {diferencia_C0:.3f}  <- cercana a 0 = INDEPENDIENTES")


#  Graficar la comparación en 3 paneles
fig, axes = plt.subplots(1, 3, figsize=(14, 5))    # Crea una figura con 3 subgráficas en una fila
fig.suptitle(                                        # Pone un título general a toda la figura
    "Independencia Condicional\nA=Gol  B=Corrió 10km  C=Entrenó duro",
    fontsize=13, fontweight='bold'                   # Fuente grande y en negritas
)

categorias = ["P(A,B)\nreal", "P(A)xP(B)\nesperado"]  # Nombres de las dos barras en cada gráfica

#  Sin conocer C (dependencia marginal) 

valores_marg = [p_AB, p_A * p_B]                    # Lista con los dos valores a comparar
bars0 = axes[0].bar(                                 # Dibuja barras en la primera subgráfica
    categorias, valores_marg,                        # Usa las etiquetas y valores definidos arriba
    color=['tomato', 'steelblue'], width=0.5         # Colores distintos para distinguir las barras
)
axes[0].set_title("Sin conocer C\n(son DEPENDIENTES)", fontsize=11)  # Título de esta subgráfica
axes[0].set_ylabel("Probabilidad")                   # Etiqueta del eje vertical
axes[0].set_ylim(0, 0.8)                             # Fija el rango del eje Y entre 0 y 0.8
axes[0].grid(True, alpha=0.3, axis='y')              # Agrega cuadrícula horizontal semitransparente
for bar, val in zip(bars0, valores_marg):            # Recorre cada barra junto con su valor
    axes[0].text(                                    # Escribe el número encima de cada barra
        bar.get_x() + bar.get_width() / 2,           # Posición X: centro de la barra
        val + 0.01,                                  # Posición Y: justo encima de la barra
        f"{val:.3f}",                                # Texto: el valor con 3 decimales
        ha='center', fontweight='bold'               # Centrado y en negritas
    )

# Gráfica 2: Dado C=1 

valores_C1 = [p_AB_C1, p_A_C1 * p_B_C1]            # Lista con los dos valores condicionados a C=1
bars1 = axes[1].bar(                                 # Dibuja barras en la segunda subgráfica
    categorias, valores_C1,                          # Mismas etiquetas, nuevos valores
    color=['mediumseagreen', 'mediumseagreen'], width=0.5  # Ambas barras en verde
)
axes[1].set_title("Dado C=1 (si entrenó)\n(son INDEPENDIENTES)", fontsize=11)  # Título de la subgráfica
axes[1].set_ylabel("Probabilidad")                   # Etiqueta del eje Y
axes[1].set_ylim(0, 0.8)                             # Mismo rango para comparar visualmente
axes[1].grid(True, alpha=0.3, axis='y')              # Cuadrícula horizontal
for bar, val in zip(bars1, valores_C1):              # Recorre barras y valores
    axes[1].text(                                    # Escribe el número encima de cada barra
        bar.get_x() + bar.get_width() / 2,           # Centro horizontal de la barra
        val + 0.01,                                  # Ligeramente por encima del tope
        f"{val:.3f}",                                # Valor numérico con 3 decimales
        ha='center', fontweight='bold'               # Centrado y negrita
    )

valores_C0 = [p_AB_C0, p_A_C0 * p_B_C0]            # Lista con los dos valores condicionados a C=0
bars2 = axes[2].bar(                                 # Dibuja barras en la tercera subgráfica
    categorias, valores_C0,                          # Mismas etiquetas, nuevos valores
    color=['mediumpurple', 'mediumpurple'], width=0.5  # Ambas barras en morado
)
axes[2].set_title("Dado C=0 (no entrenó)\n(son INDEPENDIENTES)", fontsize=11)  # Título de la subgráfica
axes[2].set_ylabel("Probabilidad")                   # Etiqueta del eje Y
axes[2].set_ylim(0, 0.8)                             # Mismo rango para comparar fácilmente
axes[2].grid(True, alpha=0.3, axis='y')              # Cuadrícula horizontal
for bar, val in zip(bars2, valores_C0):              # Recorre barras y valores
    axes[2].text(                                    # Escribe el número encima de cada barra
        bar.get_x() + bar.get_width() / 2,           # Centro de la barra en X
        val + 0.01,                                  # Encima del tope de la barra
        f"{val:.3f}",                                # Texto con 3 decimales
        ha='center', fontweight='bold'               # Centrado y en negritas
    )

plt.tight_layout()                                   # Ajusta automáticamente el espacio entre subgráficas
plt.savefig("independencia_condicional.png",         # Guarda la figura como archivo PNG
            dpi=150, bbox_inches='tight')            # Alta resolución y sin bordes extra
plt.show()                                           # Muestra la figura en pantalla


# CONCLUSIÓN FINAL
print("\n" + "=" * 52)                               # Línea en blanco y separador visual
print("   CONCLUSIÓN")                               # Título del bloque final
print("=" * 52)                                      # Línea decorativa
print(f"  Sin C   -> diferencia = {diferencia_marginal:.3f}  (DEPENDIENTES)")   # Sin C: diferencia grande
print(f"  Con C=1 -> diferencia = {diferencia_C1:.3f}  (INDEPENDIENTES)")       # Con C=1: diferencia ~0
print(f"  Con C=0 -> diferencia = {diferencia_C0:.3f}  (INDEPENDIENTES)")       # Con C=0: diferencia ~0
print()                                              # Línea en blanco para legibilidad
print("  Conocer si el jugador entrenó duro explica")      # Interpretación en lenguaje natural
print("  la relación entre goles y kilómetros corridos.")  # C es la causa que conecta A y B
print("  Una vez que sabes C, A y B ya no se afectan.")    # Al condicionar en C, la dependencia desaparece
print("=" * 52)                                      # Línea decorativa final