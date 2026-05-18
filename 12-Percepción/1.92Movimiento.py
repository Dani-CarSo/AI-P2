#92
#Movimiento

# 1. ESTRUCTURA PROFUNDA (La idea base en la mente)
# El objeto ("pescado") está después del verbo ("come")
frase_base = {
    "Sujeto": "el gato",
    "Verbo": "come",
    "Objeto": "pescado"
}

def aplicar_movimiento_wh(estructura):
    # Paso A: Identificar el elemento a extraer (el Objeto)
    # En gramática, esto se llama "Marcado de Caso"
    elemento_movido = estructura["Objeto"]
    
    # Paso B: Sustituir el objeto por un pronombre interrogativo (Wh-word)
    # 'pescado' se convierte en 'qué'
    pronombre = "qué"
    
    # Paso C: Realizar el MOVIMIENTO (Desplazamiento a la izquierda)
    # Movemos el pronombre al inicio de la oración
    # Dejamos una "huella" (t) en la posición original para recordar la relación
    posicion_final = f"{pronombre} {estructura['Verbo']} {estructura['Sujeto']} [huella_t]"
    
    return posicion_final

# --- EJECUCIÓN ---
print("--- SIMULACIÓN DE MOVIMIENTO SINTÁCTICO ---")
# Mostramos la idea original
print(f"Estructura Profunda: {frase_base['Sujeto']} {frase_base['Verbo']} {frase_base['Objeto']}")

# Aplicamos la regla de movimiento
resultado = aplicar_movimiento_wh(frase_base)

# Mostramos la estructura superficial (la que decimos al hablar)
print(f"Estructura Superficial: {resultado}")