#50
#Red Bayesiana

# No necesitamos librerías externas: solo Python puro + matplotlib
import random                            # Para simular lanzamientos de probabilidad
import matplotlib.pyplot as plt          # Para dibujar la red y los resultados
import matplotlib.patches as mpatches   # Para dibujar flechas y formas en la gráfica

random.seed(42)                          # Fija la semilla: resultados iguales en cada ejecución

# Definir las Tablas de Probabilidad Condicional (CPT)
# Cada tabla dice: dada cierta condición, ¿cuál es la prob. de que ocurra?
# Nodo raíz: Lesionado (no tiene padres, probabilidad fija)
P_lesionado = 0.20                       # 20% de probabilidad de que el jugador esté lesionado

# Nodo raíz: Clima favorable (no tiene padres, probabilidad fija)
P_buen_clima = 0.70                      # 70% de probabilidad de que el clima sea bueno

# Nodo intermedio: ¿El jugador juega?
# Depende de si está lesionado Y del clima
# Formato: P_juega[lesionado][buen_clima] = probabilidad de que juegue
P_juega = {
    (False, False): 0.40,                # No lesionado, mal clima → juega con 40%
    (False, True):  0.90,                # No lesionado, buen clima → juega con 90%
    (True,  False): 0.05,                # Lesionado, mal clima → juega con 5% (casi nunca)
    (True,  True):  0.15,                # Lesionado, buen clima → juega con 15% (muy poco)
}

# Nodo hoja: ¿El equipo gana?
# Depende solo de si el jugador juega o no
# Formato: P_gana[juega] = probabilidad de ganar
P_gana = {
    True:  0.75,                         # Si el jugador juega → 75% de ganar
    False: 0.35,                         # Si el jugador NO juega → 35% de ganar
}

# Función para simular UN partido usando la red
# Recorre la red de arriba hacia abajo (de causas a efectos)

def simular_partido():                   # Define la función que simula un solo partido
    """Simula un partido recorriendo la red bayesiana nodo por nodo."""

    # Nodo 1: ¿Está lesionado? (nodo raíz, sin padres)
    lesionado = random.random() < P_lesionado    # True si el número aleatorio cae dentro del 20%

    # Nodo 2: ¿Hay buen clima? (nodo raíz, sin padres)
    buen_clima = random.random() < P_buen_clima  # True si el número aleatorio cae dentro del 70%

    # Nodo 3: ¿Juega el partido? (depende de lesionado y buen_clima)
    prob_juega = P_juega[(lesionado, buen_clima)]       # Busca la probabilidad en la tabla CPT
    juega      = random.random() < prob_juega            # True si el número aleatorio < esa probabilidad

    # Nodo 4: ¿Gana el equipo? (depende solo de si juega)
    prob_gana = P_gana[juega]                    # Busca la probabilidad según si juega o no
    gana      = random.random() < prob_gana      # True si el número aleatorio < esa probabilidad

    return lesionado, buen_clima, juega, gana    # Devuelve el resultado de los 4 nodos

# Simular muchos partidos y contar resultados
N = 50_000                               # Número de partidos a simular

# Contadores para estadísticas generales
conteo_lesionado  = 0                    # Cuántas veces estuvo lesionado
conteo_buen_clima = 0                    # Cuántas veces hubo buen clima
conteo_juega      = 0                    # Cuántas veces jugó el partido
conteo_gana       = 0                    # Cuántas veces ganó el equipo

# Contadores para inferencia condicional
gana_dado_juega     = 0                  # Partidos donde jugó Y ganó
total_dado_juega    = 0                  # Partidos donde jugó (para calcular la proporción)
gana_dado_no_juega  = 0                  # Partidos donde NO jugó pero ganó
total_dado_no_juega = 0                  # Partidos donde no jugó

for _ in range(N):                       # Repite la simulación N veces
    l, c, j, g = simular_partido()       # Desempaca los 4 resultados del partido

    if l: conteo_lesionado  += 1         # Suma 1 si estuvo lesionado
    if c: conteo_buen_clima += 1         # Suma 1 si hubo buen clima
    if j: conteo_juega      += 1         # Suma 1 si jugó
    if g: conteo_gana       += 1         # Suma 1 si ganó

    if j:                                # Si el jugador SÍ jugó...
        total_dado_juega += 1            # Cuenta este partido en el grupo "jugó"
        if g: gana_dado_juega += 1       # Y si además ganó, suma al contador de victorias

    else:                                # Si el jugador NO jugó...
        total_dado_no_juega += 1         # Cuenta este partido en el grupo "no jugó"
        if g: gana_dado_no_juega += 1    # Y si aun así ganó, suma al contador


# Calcular probabilidades estimadas
p_est_lesionado  = conteo_lesionado  / N   # Proporción de partidos con lesión
p_est_buen_clima = conteo_buen_clima / N   # Proporción de partidos con buen clima
p_est_juega      = conteo_juega      / N   # Proporción de partidos donde jugó
p_est_gana       = conteo_gana       / N   # Proporción de partidos donde ganó

# Probabilidades condicionales (inferencia)
p_gana_dado_juega    = gana_dado_juega    / total_dado_juega     # P(Gana | Juega)
p_gana_dado_no_juega = gana_dado_no_juega / total_dado_no_juega  # P(Gana | No Juega)

#  Imprimir resultados en consola
print("=" * 52)                          # Línea decorativa
print(f"   RED BAYESIANA — {N:,} partidos simulados")  # Título con el número de simulaciones
print("=" * 52)                          # Línea decorativa

print("\n── Probabilidades marginales (sin condición) ──")
print(f"  P(Lesionado)   = {p_est_lesionado:.3f}   [esperado: {P_lesionado:.3f}]")   # Compara simulado vs teórico
print(f"  P(Buen clima)  = {p_est_buen_clima:.3f}   [esperado: {P_buen_clima:.3f}]") # Compara simulado vs teórico
print(f"  P(Juega)       = {p_est_juega:.3f}")      # Probabilidad de que juegue (resultado emergente)
print(f"  P(Gana)        = {p_est_gana:.3f}")       # Probabilidad de ganar (resultado emergente)

print("\n── Inferencia condicional ──")
print(f"  P(Gana | Juega)    = {p_gana_dado_juega:.3f}   [esperado: {P_gana[True]:.3f}]")   # Compara con CPT
print(f"  P(Gana | No Juega) = {p_gana_dado_no_juega:.3f}   [esperado: {P_gana[False]:.3f}]") # Compara con CPT
print("=" * 52)                          # Línea decorativa final

#  Graficar — estructura de la red + barras de resultados

fig = plt.figure(figsize=(14, 6))        # Crea la figura con tamaño amplio

# ── Subgráfica izquierda: estructura visual de la red ──

ax1 = fig.add_subplot(1, 2, 1)          # Panel izquierdo (1 fila, 2 columnas, posición 1)
ax1.set_xlim(0, 10)                     # Rango del eje X del panel
ax1.set_ylim(0, 10)                     # Rango del eje Y del panel
ax1.axis('off')                         # Oculta los ejes (solo queremos el dibujo)
ax1.set_title("Estructura de la Red Bayesiana", fontsize=12, fontweight='bold')  # Título del panel

# Dibuja los nodos como rectángulos con texto
nodos = [                                # Lista de nodos: (x, y, texto, color)
    (2.5, 8.0, "Lesionado\nP=0.20",   '#e07070'),   # Nodo superior izquierdo (rojo suave)
    (7.0, 8.0, "Buen Clima\nP=0.70",  '#70a0e0'),   # Nodo superior derecho (azul suave)
    (4.7, 5.0, "¿Juega?",             '#f0c060'),   # Nodo del medio (amarillo)
    (4.7, 2.0, "¿Gana el equipo?",    '#70c090'),   # Nodo inferior (verde)
]

for (x, y, texto, color) in nodos:      # Recorre cada nodo de la lista
    ax1.add_patch(                       # Agrega un rectángulo al panel
        mpatches.FancyBboxPatch(         # Rectángulo con esquinas redondeadas
            (x - 1.5, y - 0.6),         # Esquina inferior izquierda del rectángulo
            3.0, 1.2,                    # Ancho y alto del rectángulo
            boxstyle="round,pad=0.1",    # Estilo: bordes redondeados con padding
            facecolor=color,             # Color de relleno del nodo
            edgecolor='#333333',         # Color del borde
            linewidth=1.5                # Grosor del borde
        )
    )
    ax1.text(x, y, texto,               # Escribe el texto en el centro del nodo
             ha='center', va='center',  # Centrado horizontal y verticalmente
             fontsize=9, fontweight='bold')  # Tamaño y peso de fuente

# Dibuja las flechas entre nodos (de causa a efecto)
flechas = [                              # Lista de flechas: (x_inicio, y_inicio, dx, dy)
    (2.5, 7.4, 1.5, -1.8),             # Lesionado → Juega
    (7.0, 7.4, -1.5, -1.8),            # Buen Clima → Juega
    (4.7, 4.4, 0.0, -1.8),             # Juega → Gana
]

for (x, y, dx, dy) in flechas:         # Recorre cada flecha de la lista
    ax1.annotate("",                    # Sin texto en la flecha
        xy=(x + dx, y + dy),           # Punto de destino (punta de la flecha)
        xytext=(x, y),                 # Punto de origen (cola de la flecha)
        arrowprops=dict(               # Propiedades visuales de la flecha
            arrowstyle="->",           # Estilo: flecha con punta
            color='#333333',           # Color de la flecha
            lw=2.0                     # Grosor de la línea
        )
    )

# ── Subgráfica derecha: barras con probabilidades estimadas ──

ax2 = fig.add_subplot(1, 2, 2)          # Panel derecho (1 fila, 2 columnas, posición 2)

etiquetas = [                            # Nombres de las barras
    "P(Lesionado)", "P(Buen clima)",
    "P(Juega)", "P(Gana)",
    "P(Gana|Juega)", "P(Gana|NoJuega)"
]

valores = [                              # Valores estimados por la simulación
    p_est_lesionado, p_est_buen_clima,
    p_est_juega, p_est_gana,
    p_gana_dado_juega, p_gana_dado_no_juega
]

colores = [                              # Un color distinto para cada barra
    '#e07070', '#70a0e0',
    '#f0c060', '#70c090',
    '#a07040', '#9070c0'
]

barras = ax2.bar(                        # Dibuja todas las barras de una vez
    etiquetas, valores,                  # Etiquetas en X, valores en Y
    color=colores,                       # Colores definidos arriba
    edgecolor='#333333',                 # Borde oscuro en cada barra
    width=0.55                           # Ancho de las barras
)

for barra, val in zip(barras, valores):  # Recorre cada barra y su valor
    ax2.text(                            # Escribe el número encima de la barra
        barra.get_x() + barra.get_width() / 2,   # Centro horizontal de la barra
        val + 0.01,                      # Justo encima del tope de la barra
        f"{val:.3f}",                    # Texto con 3 decimales
        ha='center', va='bottom',        # Alineado al centro y abajo del texto
        fontsize=8, fontweight='bold'    # Tamaño y peso de la fuente
    )

ax2.set_ylim(0, 1.05)                   # El eje Y va de 0 a 1.05 (probabilidades)
ax2.set_ylabel("Probabilidad")          # Etiqueta del eje vertical
ax2.set_title("Probabilidades estimadas\n(simulación Monte Carlo)", fontsize=12, fontweight='bold')  # Título
ax2.tick_params(axis='x', rotation=30) # Rota las etiquetas del eje X para que no se encimen
ax2.grid(True, alpha=0.3, axis='y')    # Cuadrícula horizontal semitransparente

plt.tight_layout()                      # Ajusta el espaciado para que nada se encime
plt.savefig("red_bayesiana.png",        # Guarda la figura como PNG
            dpi=150, bbox_inches='tight')  # Alta resolución y sin bordes extra
plt.show()                              # Muestra la figura en pantalla

print("\nArchivo guardado: red_bayesiana.png")  # Confirma que se guardó la imagen