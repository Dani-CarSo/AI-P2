#65
#Aprendizaje Bayesiano

p_spam = 0.3
# Probabilidad inicial de que un correo sea spam (30%)

p_not_spam = 0.7
# Probabilidad inicial de que un correo NO sea spam (70%)

# -----------------------------
# Probabilidades del modelo
# -----------------------------

p_word_given_spam = 0.8
# Probabilidad de que aparezca una palabra sospechosa si el correo es spam

p_word_given_not_spam = 0.2
# Probabilidad de que aparezca la misma palabra si NO es spam

# -----------------------------
# Función de actualización Bayesiana
# -----------------------------

def bayes_update(p_spam, p_not_spam, p_ws, p_wns):
    # Esta función aplica el Teorema de Bayes para actualizar creencias
    
    evidence = (p_ws * p_spam) + (p_wns * p_not_spam)
    # Calcula la evidencia total (normalización)
    # Es la probabilidad de observar el dato en general
    
    new_spam = (p_ws * p_spam) / evidence
    # Calcula la probabilidad posterior de que sea spam
    
    new_not_spam = (p_wns * p_not_spam) / evidence
    # Calcula la probabilidad posterior de que NO sea spam
    
    return new_spam, new_not_spam
    # Devuelve las nuevas probabilidades actualizadas

# -----------------------------
# Mensajes iniciales del sistema
# -----------------------------

print("=== APRENDIZAJE BAYESIANO INTERACTIVO ===")
# Título del programa

print("Ingresa 1 si aparece palabra sospechosa")
# Instrucción: evidencia positiva

print("Ingresa 0 si NO aparece")
# Instrucción: evidencia negativa

print("Escribe 'salir' para terminar\n")
# Permite terminar el programa

# -----------------------------
# Contador de pasos
# -----------------------------

step = 0
# Lleva registro de cuántas evidencias se han ingresado

# -----------------------------
# Bucle interactivo principal
# -----------------------------

while True:
    # Inicia un ciclo infinito hasta que el usuario decida salir
    
    user_input = input("Evidencia (0/1): ")
    # El usuario introduce nueva evidencia
    
    if user_input.lower() == "salir":
        # Si el usuario escribe "salir", termina el programa
        break
    
    if user_input not in ["0", "1"]:
        # Validación: solo se aceptan 0 o 1
        print("Entrada inválida. Usa 0, 1 o 'salir'\n")
        continue
        # Regresa al inicio del ciclo sin ejecutar más código
    
    obs = int(user_input)
    # Convierte la entrada a número entero (0 o 1)
    
    step += 1
    # Incrementa el contador de pasos
    
    print(f"\n--- Paso {step} ---")
    # Muestra el número de iteración actual
    
    # -----------------------------
    # Actualización Bayesiana
    # -----------------------------
    
    if obs == 1:
        # Si hay evidencia de palabra sospechosa
        
        p_spam, p_not_spam = bayes_update(
            p_spam, p_not_spam,
            p_word_given_spam,
            p_word_given_not_spam
        )
        # Actualiza probabilidades usando evidencia positiva
    
    else:
        # Si NO hay palabra sospechosa
        
        p_spam, p_not_spam = bayes_update(
            p_spam, p_not_spam,
            1 - p_word_given_spam,
            1 - p_word_given_not_spam
        )
        # Actualiza probabilidades usando evidencia negativa
    
    # -----------------------------
    # Mostrar resultados actuales
    # -----------------------------
    
    print(f"Probabilidad SPAM:     {p_spam:.3f}")
    # Muestra probabilidad actual de spam
    
    print(f"Probabilidad NO SPAM:  {p_not_spam:.3f}")
    # Muestra probabilidad actual de no spam
    
    # -----------------------------
    # Decisión del sistema
    # -----------------------------
    
    if p_spam > p_not_spam:
        print("Estado actual: SPAM 🚨")
        # Si la probabilidad de spam es mayor, clasifica como spam
    else:
        print("Estado actual: NO SPAM ✅")
        # Si no, clasifica como correo normal
    
    print("-" * 40)
    # Separador visual entre pasos

# -----------------------------
# Resultado final
# -----------------------------

print("\n=== RESULTADO FINAL ===")
# Encabezado del resultado final

if p_spam > p_not_spam:
    print("El sistema concluye: SPAM")
    # Decisión final del modelo
else:
    print("El sistema concluye: NO SPAM")
    # Decisión final del modelo