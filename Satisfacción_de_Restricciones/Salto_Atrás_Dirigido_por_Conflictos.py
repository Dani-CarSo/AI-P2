#21
#Salto

# Lista de variables del problema, en el orden en que se asignarán
variables = ["A", "B", "C"]
 
# Dominios: valores posibles para cada variable
dominios = {
    "A": [1, 2],   # A puede valer 1 o 2
    "B": [1, 2],   # B puede valer 1 o 2
    "C": [1, 2],   # C puede valer 1 o 2
}
 
# Restricciones binarias: pares de variables que NO pueden tener el mismo valor.
# Se guardan en un set de tuplas para búsqueda rápida O(1).
# La restricción es simétrica: (A,B) y (B,A) significan que A ≠ B.
restricciones = {
    ("A", "B"),   # A debe ser distinta de B
    ("B", "A"),   # B debe ser distinta de A (misma restricción, dirección opuesta)
    ("B", "C"),   # B debe ser distinta de C
    ("C", "B"),   # C debe ser distinta de B
}
 
 
def consistente(var, valor, asignacion):
    
    # Conjunto donde acumulamos las variables con las que hay conflicto
    conflictos = set()
 
    # Recorremos todas las variables ya asignadas
    for v in asignacion:
 
        # Revisamos si existe una restricción entre `var` y `v`
        if (var, v) in restricciones and asignacion[v] == valor:
            # Hay restricción Y ambas tienen el mismo valor → conflicto
            conflictos.add(v)
 
    # Si conflictos está vacío no hay problema; si tiene elementos, hay conflicto
    return len(conflictos) == 0, conflictos
 
 
def cbj(asignacion, nivel):
    
    # CASO BASE: todas las variables han sido asignadas → solución encontrada
    if nivel == len(variables):
        return asignacion, set()
 
    # Variable que toca asignar en este nivel
    var = variables[nivel]
 
    # Acumula todos los conflictos encontrados al probar los valores del dominio
    conflicto_total = set()
 
    # Probamos cada valor posible del dominio de `var`
    for valor in dominios[var]:
 
        # Verificamos si este valor es compatible con lo ya asignado
        es_valido, conflictos = consistente(var, valor, asignacion)
 
        if es_valido:
            # El valor es compatible: lo asignamos y seguimos al nivel siguiente
            asignacion[var] = valor
 
            # Llamada recursiva para asignar la siguiente variable
            resultado, conflicto = cbj(asignacion, nivel + 1)
 
            if resultado:
                # La rama terminó en solución → propagamos hacia arriba
                return resultado, set()
 
            # La rama falló. Comprobamos si el conflicto involucra a esta variable.
            # Si el conflicto NO menciona a `var`, esta variable no es culpable:
            # no tiene sentido seguir probando sus otros valores.
            # → SALTO ATRÁS: devolvemos el conflicto sin modificarlo
            if var not in conflicto:
                return None, conflicto
 
            # El conflicto sí involucra a `var`, así que probar otro valor
            # de `var` puede ayudar. Acumulamos los conflictos con otras variables
            # (quitamos a `var` porque ya la estamos manejando aquí)
            conflicto_total |= (conflicto - {var})
 
            # Deshacemos la asignación de `var` para probar el siguiente valor
            del asignacion[var]
 
        else:
            # El valor es inválido desde el principio (conflicto directo).
            # Guardamos con qué variables chocó para saber a dónde saltar.
            conflicto_total |= conflictos
 
    # Agotamos todos los valores de `var` sin éxito.
    # Devolvemos el conjunto total de conflictos para que el nivel superior
    # decida si debe seguir probando o saltar más atrás.
    return None, conflicto_total

 
# Arrancamos CBJ con asignación vacía y desde el nivel 0 (primera variable)
solucion, _ = cbj({}, 0)
 
print("Solución:")
print(solucion)