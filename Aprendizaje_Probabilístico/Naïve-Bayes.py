#66
#Naïve-Bayes


import numpy as np
# Importa NumPy para manejar números y cálculos probabilísticos

# -----------------------------
# Dataset simple (entrenamiento ficticio)
# -----------------------------

vocab = ["dinero", "gratis", "hola", "oferta", "reunion"]
# Lista de palabras que el modelo puede reconocer

# Probabilidad de cada palabra dado que es SPAM
p_word_given_spam = {
    "dinero": 0.7,
    "gratis": 0.9,
    "hola": 0.1,
    "oferta": 0.8,
    "reunion": 0.05
}
# Estas probabilidades representan qué tan común es cada palabra en spam

# Probabilidad de cada palabra dado que NO es spam
p_word_given_not_spam = {
    "dinero": 0.1,
    "gratis": 0.05,
    "hola": 0.6,
    "oferta": 0.2,
    "reunion": 0.7
}
# Estas probabilidades representan palabras comunes en mensajes normales

# -----------------------------
# Probabilidades iniciales (prior)
# -----------------------------

p_spam = 0.4
# Creencia inicial: 40% de mensajes son spam

p_not_spam = 0.6
# 60% no son spam

# -----------------------------
# Función Naïve Bayes
# -----------------------------

def naive_bayes(message_words):
    global p_spam, p_not_spam
    # Permite modificar las variables globales dentro de la función

    # Inicializamos probabilidades con los priors
    spam_score = p_spam
    # Probabilidad inicial de spam

    not_spam_score = p_not_spam
    # Probabilidad inicial de no spam

    # -----------------------------
    # Multiplicación de probabilidades (Naïve assumption)
    # -----------------------------
    
    for word in message_words:
        # Recorre cada palabra del mensaje
        
        if word in p_word_given_spam:
            # Si la palabra existe en el vocabulario
            
            spam_score *= p_word_given_spam[word]
            # Multiplica la probabilidad de spam por la probabilidad de la palabra en spam
            
            not_spam_score *= p_word_given_not_spam[word]
            # Multiplica la probabilidad de no spam por la probabilidad de la palabra en no spam

    # -----------------------------
    # Normalización (Bayes)
    # -----------------------------
    
    total = spam_score + not_spam_score
    # Suma total de probabilidades

    spam_prob = spam_score / total
    # Probabilidad final de spam

    not_spam_prob = not_spam_score / total
    # Probabilidad final de no spam

    return spam_prob, not_spam_prob
    # Devuelve las probabilidades finales

# -----------------------------
# Interacción con el usuario
# -----------------------------

print("=== NAÏVE BAYES INTERACTIVO ===")
# Título del sistema

print("Palabras disponibles:", vocab)
# Muestra vocabulario permitido

print("Escribe un mensaje separado por espacios")
# Instrucción al usuario

print("Ejemplo: gratis dinero oferta\n")
# Ejemplo de entrada

# -----------------------------
# Loop interactivo
# -----------------------------

while True:
    # Bucle infinito hasta que el usuario decida salir

    user_input = input("Mensaje (o 'salir'): ")
    # El usuario escribe un mensaje

    if user_input.lower() == "salir":
        # Condición de salida
        break

    message_words = user_input.lower().split()
    # Convierte el mensaje en lista de palabras

    spam_prob, not_spam_prob = naive_bayes(message_words)
    # Aplica el modelo Naïve Bayes

    print("\n--- RESULTADO ---")
    # Separador visual

    print(f"Probabilidad SPAM:     {spam_prob:.3f}")
    # Muestra probabilidad de spam

    print(f"Probabilidad NO SPAM:  {not_spam_prob:.3f}")
    # Muestra probabilidad de no spam

    if spam_prob > not_spam_prob:
        print("Clasificación: SPAM ")
        # Si es mayor la probabilidad de spam
    else:
        print("Clasificación: NO SPAM ")
        # Si no, es mensaje normal

    print("-" * 40)
    # Separador entre iteraciones