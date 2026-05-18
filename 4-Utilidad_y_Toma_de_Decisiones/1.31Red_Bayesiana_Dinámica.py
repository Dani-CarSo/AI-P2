#31
#Red Bayesiana Dinámica

# Definimos los estados ocultos del sistema
# (no los vemos directamente, pero queremos inferirlos)
estados = ["normal", "fallando"]

# Creencia inicial: qué tan probable es cada estado al inicio
belief = {
    "normal": 0.8,     # 80% de probabilidad de que esté bien
    "fallando": 0.2    # 20% de probabilidad de falla
}

# Probabilidades de transición
# Representa cómo cambia el estado con el tiempo
transicion = {
    "normal": {"normal": 0.7, "fallando": 0.3},   # si está normal, puede fallar
    "fallando": {"normal": 0.2, "fallando": 0.8}  # si falla, es probable que siga fallando
}

# Probabilidades de observación
# Qué tan probable es ver cierta evidencia dado un estado
observacion_prob = {
    "normal": {
        "ruido_bajo": 0.8,   # si está normal, lo más probable es poco ruido
        "ruido_alto": 0.2,
        "temp_baja": 0.7,
        "temp_alta": 0.3
    },
    "fallando": {
        "ruido_bajo": 0.2,   # si falla, suele haber ruido alto
        "ruido_alto": 0.8,
        "temp_baja": 0.3,
        "temp_alta": 0.7
    }
}

# Función para normalizar probabilidades (que sumen 1)
def normalizar(dist):
    total = sum(dist.values())  # suma de todas las probabilidades
    return {k: v / total for k, v in dist.items()}  # divide cada valor entre el total

# Preguntamos cuántas observaciones quiere ingresar el usuario
pasos = int(input("¿Cuántas observaciones quieres ingresar?: "))

# Mostramos las opciones disponibles
print("\nObservaciones posibles: ruido_bajo, ruido_alto, temp_baja, temp_alta\n")

# Bucle principal (tiempo)
for t in range(pasos):
    
    print(f"\n--- Tiempo {t+1} ---")
    
    # Pedimos la observación al usuario
    obs = input("Ingresa observación: ").lower()
    
    # Diccionario para guardar las nuevas creencias
    nuevo_belief = {}
    
    # FILTRADO BAYESIANO
    # Recorremos cada estado posible actual
    for estado_actual in estados:
        
        suma = 0  # acumulador
        
        # SUMA de probabilidades de todos los estados anteriores
        for estado_prev in estados:
            
            # Fórmula: P(prev) * P(actual | prev)
            suma += belief[estado_prev] * transicion[estado_prev][estado_actual]
        
        # Multiplicamos por la probabilidad de la observación
        if obs in observacion_prob[estado_actual]:
            
            # Aplicamos evidencia
            nuevo_belief[estado_actual] = suma * observacion_prob[estado_actual][obs]
        
        else:
            # Si la observación no existe, no afecta
            nuevo_belief[estado_actual] = suma
    
    # Normalizamos para que las probabilidades sumen 1
    belief = normalizar(nuevo_belief)
    
    # Mostramos resultados actuales
    print("Probabilidad actual:")
    for estado, prob in belief.items():
        print(f"  {estado}: {round(prob, 3)}")

# Elegimos el estado con mayor probabilidad final
estado_final = max(belief, key=belief.get)

# Mostramos resultado final
print("\nEstado más probable de la máquina:", estado_final)