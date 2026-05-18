#82
#Gramática Probabilística Lexicalizada

import random # Importamos para poder elegir opciones basadas en probabilidad

# 1. EL DICCIONARIO DE DEPENDENCIAS (El núcleo del modelo)
# Aquí definimos que el Verbo es el "jefe". Cada verbo tiene su propio
# conjunto de sustantivos probables (objetos).
# Esto evita que el sistema diga cosas como "leer pescado".
dependencias = {
    "comer": {
        "pescado": 0.7, # 70% de probabilidad de comer pescado
        "carne": 0.2,    # 20% de probabilidad de comer carne
        "manzanas": 0.1  # 10% de probabilidad de comer manzanas
    },
    "leer": {
        "libros": 0.8,   # Es muy probable leer libros
        "revistas": 0.1, # Menos probable revistas
        "noticias": 0.1  # 10% de probabilidad para noticias
    }
}

# 2. FUNCIÓN DE GENERACIÓN LEXICALIZADA
def generar_frase_lexicalizada():
    # Paso A: Elegir la 'cabeza' o palabra principal de la frase
    # En este caso, elegimos un verbo al azar de nuestras claves
    verbo_cabeza = random.choice(list(dependencias.keys()))
    
    # Paso B: Filtrar el contexto
    # Obtenemos solo los objetos que tienen sentido con el verbo elegido
    # Si elegimos 'leer', solo miraremos {'libros', 'revistas', 'noticias'}
    opciones_asociadas = dependencias[verbo_cabeza]
    
    # Paso C: Preparar las opciones y sus pesos para el dado probabilístico
    palabras_posibles = list(opciones_asociadas.keys()) # Lista de palabras (ej. ['libros', 'revistas'])
    probabilidades = list(opciones_asociadas.values())   # Lista de pesos (ej. [0.8, 0.1])
    
    # Paso D: Selección ponderada
    # Elegimos un objeto basado estrictamente en las probabilidades del verbo
    objeto_elegido = random.choices(palabras_posibles, weights=probabilidades, k=1)[0]
    
    # Devolvemos la estructura final "lexicalizada"
    return f"Sujeto -> {verbo_cabeza} (cabeza) -> {objeto_elegido}"

# --- EJECUCIÓN DEL MODELO ---
print("--- RESULTADOS DE LA GRAMÁTICA LEXICALIZADA ---")
# Generamos 5 ejemplos para ver cómo el verbo siempre arrastra a un objeto coherente
for i in range(5):
    print(f"Ejemplo {i+1}: {generar_frase_lexicalizada()}")