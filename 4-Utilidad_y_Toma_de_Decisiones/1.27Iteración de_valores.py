#27
# Iteracion de valores

# Pedimos al usuario los estados separados por comas y los guardamos en una lista
estados = input("Ingresa los estados separados por coma (ej: A,B,C): ").split(",")

# Pedimos las acciones posibles y las convertimos en lista
acciones = input("Ingresa las acciones separadas por coma (ej: izquierda,derecha): ").split(",")

# Creamos un diccionario vacío donde guardaremos las transiciones
transiciones = {}

# Mensajes de ayuda para el usuario
print("\n--- Definir transiciones ---")
print("Formato: probabilidad,nuevo_estado,recompensa")
print("Ejemplo: 1.0,B,5\n")

# Recorremos cada estado
for estado in estados:
    # Para cada estado recorremos cada acción
    for accion in acciones:
        
        # Preguntamos si quiere definir esa transición
        resp = input(f"¿Definir transición para ({estado}, {accion})? (si/no): ").lower()
        
        # Si responde "si"
        if resp == "si":
            
            # Creamos una lista para guardar múltiples resultados posibles
            lista = []
            
            # Bucle para ingresar varias transiciones
            while True:
                
                # Pedimos los datos o la palabra "fin"
                datos = input("Ingresa transición o 'fin': ")
                
                # Si escribe "fin", salimos del ciclo
                if datos == "fin":
                    break
                
                # Separamos los datos en probabilidad, nuevo estado y recompensa
                prob, nuevo_estado, recompensa = datos.split(",")
                
                # Guardamos la transición como tupla (probabilidad, estado destino, recompensa)
                lista.append((float(prob), nuevo_estado, float(recompensa)))
            
            # Guardamos todas las transiciones en el diccionario
            transiciones[(estado, accion)] = lista

# Pedimos el factor de descuento (qué tanto importan recompensas futuras)
gamma = float(input("\nIngresa el factor de descuento (ej: 0.9): "))

# Pedimos cuántas iteraciones queremos ejecutar
iteraciones = int(input("Número de iteraciones: "))

# Inicializamos el valor de cada estado en 0
V = {estado: 0 for estado in estados}

# Mostramos valores iniciales
print("\nValores iniciales:", V)

# ALGORITMO DE ITERACIÓN DE VALORES
# Repetimos el proceso varias veces
for i in range(iteraciones):
    
    # Copiamos los valores actuales
    nuevo_V = V.copy()
    
    # Recorremos cada estado
    for estado in estados:
        
        # Lista para guardar el valor de cada acción
        valores_acciones = []
        
        # Probamos cada acción
        for accion in acciones:
            
            # Verificamos que exista transición definida
            if (estado, accion) in transiciones:
                
                # Inicializamos el valor de la acción
                valor = 0
                
                # Recorremos cada posible resultado de la acción
                for prob, nuevo_estado, recompensa in transiciones[(estado, accion)]:
                    
                    # Fórmula de iteración de valores:
                    # recompensa + (gamma * valor futuro)
                    valor += prob * (recompensa + gamma * V[nuevo_estado])
                
                # Guardamos el valor calculado
                valores_acciones.append(valor)
        
        # Si hay acciones posibles
        if valores_acciones:
            
            # Elegimos la mejor (la de mayor valor)
            nuevo_V[estado] = max(valores_acciones)
    
    # Actualizamos los valores
    V = nuevo_V
    
    # Mostramos resultados de la iteración
    print(f"\nIteración {i+1}: {V}")

# Mostramos valores finales
print("\nValores finales:", V)