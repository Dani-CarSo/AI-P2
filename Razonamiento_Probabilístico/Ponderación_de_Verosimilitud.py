#56
#Ponderación de Verosimilitud

# Importamos random para generar números aleatorios
import random

# Mostramos el título del programa
print(" Detector de Spam ")

# Preguntamos cuántas palabras sospechosas tiene el mensaje
palabras_spam = int(input("¿Cuántas palabras sospechosas tiene el mensaje?: "))

# Probabilidad inicial de que sea spam
# Antes de revisar el mensaje
probabilidad_spam = 0.4

# Mostramos la probabilidad inicial
print("\nProbabilidad inicial:", probabilidad_spam)


# PONDERACIÓN DE VEROSIMILITUD
# Ajustamos la probabilidad usando evidencia
# Si tiene muchas palabras sospechosas
if palabras_spam >= 5:

    # Aumentamos mucho la probabilidad
    probabilidad_spam *= 2

# Si tiene pocas palabras sospechosas
elif palabras_spam >= 2:

    # Aumentamos un poco la probabilidad
    probabilidad_spam *= 1.3

# Si no tiene casi palabras sospechosas
else:

    # Disminuimos la probabilidad
    probabilidad_spam *= 0.5

# NORMALIZACIÓN
# Evitamos que la probabilidad sea mayor a 1
# Si la probabilidad supera 1
if probabilidad_spam > 1:

    # La dejamos exactamente en 1
    probabilidad_spam = 1

# Mostramos la probabilidad final
print("\nProbabilidad final:", round(probabilidad_spam, 2))


# DECISIÓN FINAL
# Si la probabilidad es alta
if probabilidad_spam >= 0.7:

    # El mensaje se considera spam
    print("El mensaje probablemente es SPAM")

# Si la probabilidad es baja
else:

    # El mensaje parece normal
    print("El mensaje parece normal")