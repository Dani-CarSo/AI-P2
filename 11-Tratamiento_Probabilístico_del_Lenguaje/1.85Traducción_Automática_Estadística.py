#85
#Traducción Automática Estadística

import random # Importamos para posibles selecciones entre opciones con igual peso

# 1. EL MODELO DE TRADUCCIÓN (P(f|e))
# Este diccionario representa lo que el sistema aprendió de un corpus paralelo.
# Mapea palabras en español a sus posibles traducciones en inglés con una probabilidad.
modelo_traduccion = {
    "el": {"the": 0.9, "a": 0.1},      # "el" suele ser "the", pero a veces "a"
    "gato": {"cat": 0.8, "tom": 0.2},   # "gato" es casi siempre "cat"
    "come": {"eats": 0.7, "is eating": 0.3}, # El verbo tiene dos formas posibles
    "pescado": {"fish": 1.0}            # "pescado" solo tiene una traducción aquí
}

# 2. EL MODELO DE LENGUAJE (P(e))
# Este modelo solo conoce el inglés. Su función es decir qué tan fluida es una frase.
# Ayuda a decidir si "the cat eats" es mejor que "cat the eats".
modelo_lenguaje = {
    "the cat eats": 0.5,
    "the cat eats fish": 0.4,
    "a cat eats": 0.1
}

def traducir_estadistico(frase_fuente):
    # Paso A: Pre-procesamiento
    # Convertimos la frase a minúsculas y la dividimos en una lista de palabras
    palabras = frase_fuente.lower().split()
    
    # Paso B: Fase de "Decodificación" (Traducción palabra por palabra)
    # Aquí buscamos en el modelo de traducción la opción con mayor probabilidad
    frase_traducida_lista = []
    for p in palabras:
        if p in modelo_traduccion:
            # max() busca la palabra con el valor (probabilidad) más alto en el diccionario
            mejor_palabra = max(modelo_traduccion[p], key=modelo_traduccion[p].get)
            frase_traducida_lista.append(mejor_palabra)
    
    # Paso C: Reconstrucción de la frase en el idioma destino
    # Unimos las palabras elegidas con espacios para formar una cadena de texto
    candidata = " ".join(frase_traducida_lista)
    
    # Paso D: Evaluación de Fluidez
    # Consultamos el modelo de lenguaje para ver qué tan "natural" es la frase resultante.
    # Si la frase no existe en el modelo, asignamos una probabilidad mínima (0.01)
    probabilidad_fluidez = modelo_lenguaje.get(candidata, 0.01)
    
    return candidata, probabilidad_fluidez

# --- PRUEBA DEL TRADUCTOR ---
texto_espanol = "el gato come"
# Ejecutamos la función y recibimos la frase y su puntaje de confianza
resultado, score = traducir_estadistico(texto_espanol)

print(f"Entrada (Español): {texto_espanol}")
print(f"Salida (Inglés): {resultado}")
print(f"Nivel de fluidez calculado: {score:.2%}")