#83
#Extracción de Información

# 1. EL TEXTO DE ENTRADA (Datos no estructurados)
# Este es el lenguaje natural tal cual viene de un artículo o noticia
texto = "Satya Nadella es el CEO de Microsoft y Sundar Pichai lidera Google"

# 2. DICCIONARIOS DE ENTIDADES (Simulación de NER - Named Entity Recognition)
# En IA, primero identificamos "etiquetas": quién es persona y qué es empresa
personas = ["Satya Nadella", "Sundar Pichai"]
empresas = ["Microsoft", "Google"]

# 3. PATRONES DE RELACIÓN (Lógica de extracción)
# Definimos verbos o frases que indican que una persona pertenece a una organización
conectores = ["CEO de", "lidera", "trabaja en"]

def extraer_informacion(frase):
    # Creamos una lista vacía para almacenar los "hechos" que encontremos
    relaciones_extraidas = []
    
    # Iniciamos un ciclo para revisar cada persona que conocemos
    for p in personas:
        # Si el nombre de la persona aparece en la oración...
        if p in frase:
            # Revisamos cada empresa en nuestra lista
            for e in empresas:
                # Si la empresa también aparece en la misma oración...
                if e in frase:
                    # Buscamos si hay un conector que los una (ej. "lidera")
                    for c in conectores:
                        # Creamos una condición: ¿Aparece la secuencia Persona + Conector + Empresa?
                        # Usamos .replace para limpiar palabras de relleno como "es el"
                        if f"{p} {c} {e}" in frase or f"{p} {c} {e}" in frase.replace("es el ", ""):
                            
                            # Si hay coincidencia, guardamos el dato como una "Tripleta" (S-P-O)
                            # Esto ya es formato de base de datos (Estructurado)
                            relaciones_extraidas.append({
                                "Sujeto": p,
                                "Relacion": "TRABAJA_EN",
                                "Objeto": e
                            })
    
    # Devolvemos la lista con todos los descubrimientos
    return relaciones_extraidas

# --- EJECUCIÓN DEL PROGRAMA ---
# Llamamos a la función y guardamos los resultados en la variable 'hechos'
hechos = extraer_informacion(texto)

print("--- REPORTE DE EXTRACCIÓN ---")
# Recorremos cada hecho extraído para mostrarlo de forma limpia
for hecho in hechos:
    # Imprimimos los campos específicos (Sujeto, Vínculo y Objeto)
    print(f"ENTIDAD: {hecho['Sujeto']} | VÍNCULO: {hecho['Relacion']} | ORGANIZACIÓN: {hecho['Objeto']}")