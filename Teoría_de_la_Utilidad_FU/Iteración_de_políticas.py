#28
#Iteración de Politicas

# Lista de estados (lugares donde puedes estar)
estados = ['A', 'B', 'C']

# Acciones posibles desde cada estado
# Ejemplo: desde A puedes ir a B o C
acciones = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A']
}

# Recompensa por moverte de un estado a otro
# (estado_actual, estado_destino): puntos que ganas
recompensa = {
    ('A', 'B'): 5,
    ('A', 'C'): 10,
    ('B', 'A'): 0,
    ('B', 'C'): 2,
    ('C', 'A'): 1
}

# Factor de descuento (qué tanto importan las recompensas futuras)
gamma = 0.9

# Inicializamos el valor de cada estado en 0
# Aquí se guardará "qué tan bueno es estar en cada estado"
V = {s: 0 for s in estados}

# Diccionario vacío para la política
# Aquí se guardará qué decisión tomar en cada estado
politica = {}

# 1. ELEGIR POLÍTICA INICIAL (INTERACTIVO)
print("Elige la política inicial:")

# Recorremos cada estado para que el usuario elija acción
for s in estados:
    print(f"\nEstado {s}")  # Mostrar el estado actual
    print("Acciones disponibles:", acciones[s])  # Mostrar opciones
    
    while True:  # Repetir hasta que el usuario elija bien
        a = input("¿A dónde quieres ir?: ")  # Pedir acción
        
        if a in acciones[s]:  # Validar que la acción exista
            politica[s] = a   # Guardar decisión en la política
            break             # Salir del ciclo
        else:
            print("Acción inválida, intenta otra.")

# FUNCIÓN PARA EVALUAR LA POLÍTICA
def evaluar():
    print("\nEvaluando política...")
    
    # Repetimos varias veces para aproximar los valores
    for i in range(5):
        print(f"\nIteración {i+1}")
        
        # Recorremos cada estado
        for s in estados:
            a = politica[s]  # Acción que dicta la política
            
            # Fórmula:
            # Valor = recompensa inmediata + futuro
            nuevo = recompensa[(s, a)] + gamma * V[a]
            
            # Mostrar cálculo
            print(f"{s} -> {a} | Valor: {nuevo:.2f}")
            
            V[s] = nuevo  # Actualizar valor del estado

# FUNCIÓN PARA MEJORAR LA POLÍTICA
def mejorar():
    print("\nMejorando política...")
    
    estable = True  # Asumimos que no cambia (optimista)

    # Revisamos cada estado
    for s in estados:
        mejor_valor = -999  # Valor muy bajo inicial
        mejor_accion = None # Mejor acción encontrada

        print(f"\nEvaluando estado {s}")

        # Probamos todas las acciones posibles
        for a in acciones[s]:
            
            # Calculamos el valor de esa acción
            valor = recompensa[(s, a)] + gamma * V[a]
            
            print(f"  Acción {a} da valor {valor:.2f}")

            # Si encontramos una mejor acción, la guardamos
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_accion = a

        # Si la acción cambió, ya no es estable
        if politica[s] != mejor_accion:
            estable = False

        politica[s] = mejor_accion  # Actualizar política
        print(f"Mejor acción para {s}: {mejor_accion}")

    return estable  # Regresar si hubo cambios


# CICLO PRINCIPAL INTERACTIVO
while True:
    print("POLÍTICA ACTUAL:", politica)  # Mostrar decisiones actuales
    print("VALORES ACTUALES:", V)       # Mostrar valores actuales

    # Menú de opciones
    opcion = input(
        "\n¿Qué quieres hacer?\n"
        "1. Evaluar política\n"
        "2. Mejorar política\n"
        "3. Salir\n> "
    )

    if opcion == '1':
        evaluar()  # Ejecutar evaluación

    elif opcion == '2':
        estable = mejorar()  # Ejecutar mejora
        
        # Si ya no cambia, terminamos
        if estable:
            print("\n🎉 ¡La política ya es óptima!")
            break

    elif opcion == '3':
        break  # Salir del programa

    else:
        print("Opción inválida")

# RESULTADO FINAL

print("POLÍTICA FINAL:", politica)  # Mejor estrategia encontrada
print("VALORES FINALES:", V)       # Valores finales de cada estado