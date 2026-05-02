#19
#Comprobación Hacia Delante

def forward_checking(dominios, var, valor, restricciones):
    # Copia cada dominio para no modificar el original durante la exploración
    nuevos_dominios = {k: v.copy() for k, v in dominios.items()}
    
    # Itera sobre cada par de variables que tienen una restricción entre sí
    for (v1, v2) in restricciones:
        
        # Caso: 'var' es el primer elemento del par → su vecino afectado es v2
        if v1 == var and v2 in nuevos_dominios:
            
            # Si el valor recién asignado está en el dominio del vecino, lo elimina
            # (dos materias no pueden compartir la misma franja horaria)
            if valor in nuevos_dominios[v2]:
                nuevos_dominios[v2].remove(valor)
                
                # Si el dominio del vecino quedó vacío, no hay solución posible → aborta
                if not nuevos_dominios[v2]:
                    return None
                    
        # Caso simétrico: 'var' es el segundo elemento → su vecino afectado es v1
        if v2 == var and v1 in nuevos_dominios:
            
            # Mismo proceso: elimina el valor del dominio de v1 si está presente
            if valor in nuevos_dominios[v1]:
                nuevos_dominios[v1].remove(valor) 
                
                # Dominio vacío → fallo anticipado, retorna None
                if not nuevos_dominios[v1]:
                    return None
                    
    # Todos los vecinos siguen con opciones válidas → retorna dominios podados
    return nuevos_dominios


def backtracking_fc(asignacion, dominios, restricciones):
    
    # Si ya se asignaron todas las variables, se encontró una solución completa
    if len(asignacion) == len(dominios):
        return asignacion
    
    # Elige la primera variable que aún no tiene valor asignado
    var = [v for v in dominios if v not in asignacion][0]
    
    # Prueba cada valor disponible en el dominio actual de esa variable
    for valor in dominios[var]:
        
        # Crea una copia de la asignación actual y agrega el nuevo par variable→valor
        nueva_asignacion = asignacion.copy()
        nueva_asignacion[var] = valor
        
        # Aplica forward checking: poda los dominios de las variables vecinas
        nuevos_dominios = forward_checking(dominios, var, valor, restricciones)
        
        # Solo continúa si ningún dominio vecino quedó vacío tras la poda
        if nuevos_dominios is not None:
            
            # Llamada recursiva con la nueva asignación y los dominios podados
            resultado = backtracking_fc(nueva_asignacion, nuevos_dominios, restricciones)
            
            # Si la recursión encontró solución, la propaga hacia arriba
            if resultado:
                return resultado
                
    # Ningún valor funcionó para esta variable → retrocede (backtrack)
    return None


# Define las variables y sus dominios posibles (franjas horarias 1, 2 o 3)
dominios = {
    "Teoria de Control": [1, 2, 3],      #Teoria de Control puede ir en franja 1, 2 o 3
    "Vision Artificial": [1, 2, 3],    # Vision Artificial puede ir en franja 1, 2 o 3
    "Vibraciones Mecanicas": [1, 2, 3]    # Vibraciones Mecanicas puede ir en franja 1, 2 o 3
}

# Define qué pares de materias NO pueden estar en la misma franja
restricciones = [
    ("Teoria de Control", "Vision Artificial"),     # Teoria de Control y Vision Artificial no pueden coincidir
    ("Vision Artificial", "Vibraciones Mecanicas")   # Vision Artificial y Vibraciones Mecanicas no pueden coincidir
]

# Lanza el algoritmo con asignación vacía al inicio
solucion = backtracking_fc({}, dominios, restricciones)

# Imprime el horario resultante: {materia: franja}
print("Horario encontrado:")
print(solucion)