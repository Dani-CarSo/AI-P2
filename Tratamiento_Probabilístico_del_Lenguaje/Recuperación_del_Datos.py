#82
#Recuperación del Datos

import math # Importamos math para usar el logaritmo en el cálculo del IDF

# 1. NUESTRA BASE DE DATOS (Colección de documentos donde buscaremos)
documentos = [
    "el gato come pescado",
    "el perro ladra al gato",
    "el pajaro vuela en el cielo"
]

# 2. FUNCIÓN DE LIMPIEZA (Tokenización)
def tokenizar(texto):
    # Convertimos a minúsculas y separamos por espacios para tener una lista de palabras
    return texto.lower().split()

# 3. CÁLCULO DE TF (Term Frequency - Relevancia Local)
def calcular_tf(termino, documento):
    # Convertimos el documento en una lista de palabras
    palabras = tokenizar(documento)
    # Contamos cuántas veces aparece la palabra de búsqueda en este documento
    conteo = palabras.count(termino)
    # Dividimos el conteo entre el total de palabras (proporción o frecuencia)
    return conteo / len(palabras)

# 4. CÁLCULO DE IDF (Inverse Document Frequency - Importancia Global)
def calcular_idf(termino, todos_docs):
    # Contamos en cuántos documentos de toda la base de datos aparece la palabra
    num_docs_con_termino = sum(1 for doc in todos_docs if termino in tokenizar(doc))
    
    # Si la palabra no existe en ningún documento, evitamos división por cero
    if num_docs_con_termino == 0:
        return 0
    
    # Fórmula IDF: logaritmo de (Total de documentos / Documentos que la tienen)
    # Esto hace que palabras comunes como "el" valgan poco y palabras raras valgan mucho
    return math.log10(len(todos_docs) / num_docs_con_termino)

# 5. MOTOR DE BÚSQUEDA
def buscar(consulta, base_datos):
    # Convertimos la pregunta del usuario en una lista de palabras
    palabras_consulta = tokenizar(consulta)
    puntuaciones = []

    # Analizamos cada documento de la base de datos uno por uno
    for doc in base_datos:
        relevancia_del_documento = 0
        # Por cada palabra que el usuario escribió en su búsqueda...
        for palabra in palabras_consulta:
            # Calculamos su TF (qué tanto se menciona aquí)
            tf = calcular_tf(palabra, doc)
            # Calculamos su IDF (qué tan especial es esa palabra en general)
            idf = calcular_idf(palabra, base_datos)
            # El puntaje es la multiplicación de ambos: TF * IDF
            relevancia_del_documento += tf * idf
        
        # Guardamos el puntaje final de este documento
        puntuaciones.append(relevancia_del_documento)
    
    return puntuaciones

# --- PRUEBA DEL BUSCADOR ---
query = "el gato" # Queremos buscar algo sobre gatos
puntos = buscar(query, documentos)

print(f"Buscando: '{query}'\n")
# Mostramos los resultados ordenados por el índice del documento
for i in range(len(documentos)):
    # Mostramos la frase original y qué tan relevante la consideró el algoritmo
    print(f"Resultado {i+1}: {documentos[i]} | Score: {puntos[i]:.4f}")