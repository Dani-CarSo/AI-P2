#64
#Red Bayes Dinámica: Filtrado de Partículas

import numpy as np
# Importa NumPy, que se usa para manejar arreglos y cálculos numéricos eficientes

# Parámetros del sistema
N = 300
# Número de partículas (hipótesis del sistema). Más partículas = más precisión pero más cómputo

process_noise = 1.0
# Ruido del modelo del sistema (incertidumbre del movimiento real)

obs_noise = 2.0
# Ruido de la observación (qué tan imprecisa es la medición)

# Estado inicial
true_state = 0
# Estado real del sistema (posición inicial del objeto)

particles = np.random.uniform(-10, 10, N)
# Inicializa partículas aleatorias en un rango amplio (creencias iniciales del sistema)

weights = np.ones(N) / N
# Asigna el mismo peso a todas las partículas (distribución uniforme inicial)

step = 0
# Contador de pasos del sistema

# Funciones del sistema
def move_true(x):
    # Simula el movimiento real del sistema (estado oculto)
    return x + 1 + np.random.normal(0, process_noise)
    # Avanza +1 en cada paso y agrega ruido aleatorio (incertidumbre real)

def observe(x):
    # Simula una medición del sistema (lo que "vemos")
    return x + np.random.normal(0, obs_noise)
    # Observación ruidosa del estado real


# Inicio del proceso interactivo
print("=== FILTRADO DE PARTÍCULAS INTERACTIVO ===")
# Mensaje inicial del programa

print("Presiona ENTER para avanzar en el tiempo (o Ctrl+C para salir)\n")
# Instrucción para el usuario

# Bucle principal

while True:
    input("→ Paso siguiente...")
    # Espera interacción del usuario para avanzar el tiempo

    step += 1
    # Incrementa el contador de pasos

    # 1. Evolución del estado real
    true_state = move_true(true_state)
    # El sistema real evoluciona (pero es oculto)

    # 2. Observación del sistema
    observation = observe(true_state)
    # Se genera una medición ruidosa del estado real

    # 3. Predicción de partículas
    particles += 1 + np.random.normal(0, process_noise, N)
    # Cada partícula también evoluciona según el modelo del sistema

    # 4. Cálculo de pesos (likelihood bayesiano)
    weights = np.exp(-0.5 * (particles - observation)**2 / obs_noise**2)
    # Calcula qué tan probable es cada partícula dada la observación

    # Evita problemas numéricos (división por cero)
    weights += 1e-300

    # Normaliza los pesos para que sumen 1
    weights /= np.sum(weights)

    # 5. Estimación del estado
    estimate = np.sum(particles * weights)
    # Promedio ponderado: mejor estimación del estado real

    # 6. Re-muestreo (resampling)
    indices = np.random.choice(range(N), size=N, p=weights)
    # Selecciona partículas según su probabilidad (las buenas se repiten)

    particles = particles[indices]
    # Reemplaza el conjunto de partículas con las seleccionadas

    weights = np.ones(N) / N
    # Reinicia los pesos después del muestreo


    # Salida de resultados
    print(f"\nPaso {step}")
    # Muestra el número de iteración actual

    print(f"Estado real:      {true_state:.3f}")
    # Muestra el estado real del sistema (oculto en la vida real)

    print(f"Observación:      {observation:.3f}")
    # Muestra la medición ruidosa

    print(f"Estimación PF:    {estimate:.3f}")
    # Muestra la estimación del filtro de partículas

    print(f"Error estimación: {abs(true_state - estimate):.3f}")
    # Muestra qué tan lejos está la estimación del valor real

    print("-" * 40)
    # Separador visual para cada paso