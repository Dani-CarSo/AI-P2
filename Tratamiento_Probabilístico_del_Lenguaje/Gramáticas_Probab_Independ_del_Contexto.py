#80
#Gramáticas Probab. Independ. del Contexto

import random
import random # Importamos para elegir reglas según su probabilidad

# 1. DEFINICIÓN DE LA GRAMÁTICA (El conocimiento estructural)
# Cada clave es un "No Terminal" (una categoría gramatical)
# Cada valor es una lista de tuplas: ([componentes], probabilidad)
gramatica = {
    "O": [ (["S", "V"], 0.8), (["S", "V", "ADV"], 0.2) ], # La Oración puede ser simple o con Adverbio
    "S": [ (["Art", "N"], 1.0) ],                        # El Sujeto siempre es Artículo + Nombre
    "Art": [ (["el"], 0.7), (["un"], 0.3) ],             # "el" es más probable que "un"
    "N": [ (["gato"], 0.6), (["perro"], 0.4) ],          # "gato" tiene 60% de probabilidad
    "V": [ (["come"], 0.5), (["duerme"], 0.5) ],         # El verbo se elige 50/50
    "ADV": [ (["rapido"], 1.0) ]                         # Solo conocemos un adverbio
}

# 2. FUNCIÓN DE EXPANSIÓN RECURSIVA
def generar(simbolo):
    # Si el símbolo no está en el diccionario, es una palabra final (TERMINAL)
    # Ejemplo: "gato" no es una categoría, así que lo devolvemos tal cual
    if simbolo not in gramatica:
        return [simbolo]
    
    # Extraemos las posibles expansiones para el símbolo actual
    # Ejemplo: para "O" extraeríamos [["S", "V"], ["S", "V", "ADV"]]
    opciones = [regla[0] for regla in gramatica[simbolo]]
    
    # Extraemos las probabilidades de esas expansiones
    # Ejemplo: para "O" sería [0.8, 0.2]
    pesos = [regla[1] for regla in gramatica[simbolo]]
    
    # random.choices elige una opción basándose en los pesos (probabilidades)
    # k=1 significa que solo queremos una elección, [0] la extrae de la lista
    eleccion = random.choices(opciones, weights=pesos, k=1)[0]
    
    # Creamos una lista para ir guardando las palabras finales
    resultado = []
    
    # Por cada parte de la regla elegida, volvemos a llamar a la función (RECURSIÓN)
    for s in eleccion:
        # extend une los resultados de las ramas más profundas del árbol
        resultado.extend(generar(s))
        
    return resultado # Devuelve la lista de palabras final

# --- PRUEBA ---
# Generamos la frase empezando desde el símbolo raíz "O" (Oración)
frase_lista = generar("O")
# Unimos las palabras con espacios para que sea legible
print("Frase generada:", " ".join(frase_lista))