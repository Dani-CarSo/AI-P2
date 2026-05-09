#47
#Distribucion de probabilidad

import numpy as np                        # Librería para operaciones numéricas
import matplotlib.pyplot as plt           # Librería para graficar
from scipy import stats                   # Módulo estadístico de SciPy

# DISTRIBUCIÓN NORMAL (Gaussiana)
media = 0                                 # Centro de la campana (μ)
desviacion = 1                            # Qué tan dispersos están los datos (σ)

x = np.linspace(-4, 4, 300)              # 300 valores del eje X entre -4 y 4

pdf_normal = stats.norm.pdf(x, media, desviacion)  # Calcula la densidad de probabilidad en cada punto X


#  DISTRIBUCIÓN BINOMIAL

n = 20                                    # Número de ensayos (ej: lanzar una moneda 20 veces)
p = 0.5                                   # Probabilidad de éxito en cada ensayo (50%)

k = np.arange(0, n + 1)                  # Posibles valores: 0, 1, 2, ..., 20 éxitos

pmf_binomial = stats.binom.pmf(k, n, p)  # Probabilidad de obtener exactamente k éxitos

#  DISTRIBUCIÓN POISSON
lam = 4                                   # Promedio de eventos por intervalo (λ = lambda)

k_poisson = np.arange(0, 15)             # Rango de valores posibles: 0 a 14 eventos

pmf_poisson = stats.poisson.pmf(k_poisson, lam)  # Probabilidad de que ocurran exactamente k eventos

# GRAFICACIÓN
fig, axes = plt.subplots(1, 3, figsize=(15, 5))   # Crea 3 gráficas lado a lado

fig.suptitle("Distribuciones de Probabilidad", fontsize=16, fontweight='bold')  # Título general

# --- Gráfica 1: Normal ---
axes[0].plot(x, pdf_normal, color='steelblue', linewidth=2)   # Dibuja la curva normal
axes[0].fill_between(x, pdf_normal, alpha=0.3, color='steelblue')  # Rellena el área bajo la curva
axes[0].set_title("Normal (μ=0, σ=1)")       # Título de la gráfica
axes[0].set_xlabel("Valor de X")             # Etiqueta del eje horizontal
axes[0].set_ylabel("Densidad de Probabilidad")  # Etiqueta del eje vertical
axes[0].grid(True, alpha=0.3)                # Cuadrícula semitransparente

# Gráfica 2: Binomial 
axes[1].bar(k, pmf_binomial, color='coral', edgecolor='black', alpha=0.8)  # Barras de probabilidad
axes[1].set_title(f"Binomial (n={n}, p={p})")   # Título con parámetros
axes[1].set_xlabel("Número de Éxitos (k)")      # Etiqueta eje X
axes[1].set_ylabel("Probabilidad P(X=k)")        # Etiqueta eje Y
axes[1].grid(True, alpha=0.3, axis='y')          # Cuadrícula solo en eje Y

#  Gráfica 3: Poisson
axes[2].bar(k_poisson, pmf_poisson, color='mediumseagreen', edgecolor='black', alpha=0.8)  # Barras
axes[2].set_title(f"Poisson (λ={lam})")     # Título con lambda
axes[2].set_xlabel("Número de Eventos (k)") # Etiqueta eje X
axes[2].set_ylabel("Probabilidad P(X=k)")   # Etiqueta eje Y
axes[2].grid(True, alpha=0.3, axis='y')     # Cuadrícula solo en eje Y

plt.tight_layout()                           # Ajusta el espaciado para que no se encimen
plt.savefig("distribucion_probabilidad.png", dpi=150, bbox_inches='tight')  # Guarda la imagen
plt.show()                                   # Muestra la gráfica en pantalla


# CÁLCULOS EXTRA: valores estadísticos clave
print("=" * 45)
print("   ESTADÍSTICAS POR DISTRIBUCIÓN")
print("=" * 45)

# Normal
print("\n📊 DISTRIBUCIÓN NORMAL:")
print(f"  Media:            {media}")                      # Valor esperado
print(f"  Desv. Estándar:   {desviacion}")                 # Dispersión
print(f"  P(-1 < X < 1):    {stats.norm.cdf(1) - stats.norm.cdf(-1):.4f}")  # Regla 68%

# Binomial
media_bin = n * p                          # Fórmula: E[X] = n * p
varianza_bin = n * p * (1 - p)            # Fórmula: Var[X] = n * p * (1-p)
print("\n DISTRIBUCIÓN BINOMIAL:")
print(f"  Media:            {media_bin}")
print(f"  Varianza:         {varianza_bin}")
print(f"  P(X = 10):        {stats.binom.pmf(10, n, p):.4f}")  # Probabilidad exacta de 10 éxitos
print(f"  P(X <= 10):       {stats.binom.cdf(10, n, p):.4f}")  # Probabilidad acumulada hasta 10

# Poisson
print("\n📊 DISTRIBUCIÓN POISSON:")
print(f"  Lambda (λ):       {lam}")                        # Media e igual a la varianza
print(f"  P(X = 4):         {stats.poisson.pmf(4, lam):.4f}")   # Prob. de exactamente 4 eventos
print(f"  P(X <= 4):        {stats.poisson.cdf(4, lam):.4f}")   # Prob. acumulada hasta 4 eventos
print("=" * 45)