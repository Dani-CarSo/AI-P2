#63
#Filtros de Kalman

entrada = input("Escribe mediciones separadas por coma (ej: 10,12,11,13): ")

# Convertimos la entrada en lista de números
mediciones = [float(x.strip()) for x in entrada.split(",")]

# ---------------------------------------------------------
# VALORES INICIALES DEL FILTRO
# ---------------------------------------------------------

# Estimación inicial del estado (lo que creemos al inicio)
estimacion = 0.0

# Incertidumbre inicial (qué tan inseguro estamos)
incertidumbre = 1.0

# Ruido del proceso (qué tanto puede cambiar el sistema)
ruido_proceso = 0.1

# Ruido de medición (qué tanto error tienen los sensores)
ruido_medicion = 1.0

# ---------------------------------------------------------
# MOSTRAMOS INICIO
# ---------------------------------------------------------

print("\n--- FILTRO DE KALMAN ---\n")

# ---------------------------------------------------------
# ITERAMOS SOBRE CADA MEDICIÓN
# ---------------------------------------------------------

for i in range(len(mediciones)):

    # Tomamos la medición actual del sensor
    z = mediciones[i]

    # -----------------------------------------------------
    # 1. PREDICCIÓN
    # -----------------------------------------------------

    # La predicción del estado (modelo simple)
    prediccion = estimacion

    # La incertidumbre aumenta con el ruido del proceso
    incertidumbre = incertidumbre + ruido_proceso

    # -----------------------------------------------------
    # 2. GANANCIA DE KALMAN
    # -----------------------------------------------------

    # Calcula cuánto confiamos en la medición vs el modelo
    ganancia = incertidumbre / (incertidumbre + ruido_medicion)

    # -----------------------------------------------------
    # 3. ACTUALIZACIÓN
    # -----------------------------------------------------

    # Ajustamos la estimación con la medición
    estimacion = prediccion + ganancia * (z - prediccion)

    # Reducimos incertidumbre después de observar datos
    incertidumbre = (1 - ganancia) * incertidumbre

    # -----------------------------------------------------
    # MOSTRAMOS RESULTADOS
    # -----------------------------------------------------

    print("Medición:", z)
    print("Estimación:", round(estimacion, 3))
    print("Incertidumbre:", round(incertidumbre, 3))
    print("Ganancia Kalman:", round(ganancia, 3))
    print("---------------------------")