#79
#Modelo Probabilístico del Lenguaje: Corpus

import random # Para elegir la palabra siguiente basándonos en azar pesado
from collections import defaultdict, Counter # Estructuras para contar frecuencias

# 1. EL CORPUS: Los datos de entrenamiento (puedes añadir más frases si quieres)
corpus = "el gato come pescado el gato duerme el perro ladra el gato come carne"

# 2. PREPROCESAMIENTO: Convertimos el texto en una lista de palabras
palabras = corpus.split()

# 3. CONSTRUCCIÓN DEL MODELO (BIGRAMAS)
# Usamos un diccionario que asocia una palabra con todas las que la han seguido
modelo = defaultdict(list)

# Llenamos el modelo recorriendo el texto de dos en dos
# zip crea parejas: (el, gato), (gato, come), etc.
for i in range(len(palabras) - 1):
    palabra_actual = palabras[i]
    siguiente_palabra = palabras[i+1]
    modelo[palabra_actual].append(siguiente_palabra)

# 4. CÁLCULO DE PROBABILIDADES
# Transformamos las listas de palabras en conteos de frecuencia
probabilidades = {}
for palabra, seguidoras in modelo.items():
    # Counter nos dice cuántas veces aparece cada opción
    # Ejemplo: 'el': {'gato': 3, 'perro': 1}
    probabilidades[palabra] = Counter(seguidoras)

# 5. FUNCIÓN DE GENERACIÓN
def generar_frase(inicio, pasos=5):
    frase = [inicio] # Iniciamos la lista con la palabra elegida
    actual = inicio
    
    for _ in range(pasos):
        if actual in probabilidades:
            # Extraemos las palabras posibles y cuántas veces aparecieron (sus pesos)
            opciones = list(probabilidades[actual].keys())
            pesos = list(probabilidades[actual].values())
            
            # random.choices elige según el peso. [0] es para sacar la palabra de la lista resultante
            siguiente = random.choices(opciones, weights=pesos, k=1)[0]
            frase.append(siguiente)
            actual = siguiente # Actualizamos para la siguiente iteración
        else:
            # Si la palabra no tiene "seguidoras" en el corpus, terminamos la frase
            break
            
    return " ".join(frase)

# --- PRUEBA INTERACTIVA ---
print("--- MODELO PROBABILÍSTICO DE LENGUAJE ---")
print(f"Diccionario de probabilidades generado: {dict(probabilidades)}")
print("-" * 40)

inicio_usuario = input("Introduce palabra inicial (el / gato / perro): ").lower()

if inicio_usuario in probabilidades:
    # Generamos una frase de hasta 6 palabras
    resultado = generar_frase(inicio_usuario, pasos=5)
    print(f"\nFrase predicha: {resultado}")
else:
    print("\nLo siento, esa palabra no está en el corpus.")