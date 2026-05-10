#54
#Eliminación de variables

# Definir el factor P(D1)
# Cada cara del dado tiene probabilidad 1/6
factor_d1 = {i: 1/6 for i in range(1, 7)}  # {1: 0.166, 2: 0.166, ...}
 
# Paso 2: definir el factor P(D2), igual que D1
factor_d2 = {i: 1/6 for i in range(1, 7)}  # {1: 0.166, 2: 0.166, ...}
 
# Paso 3: definir el factor P(Suma | D1, D2)
# La suma es determinista: si D1=a y D2=b, Suma=a+b con prob 1, 0 en otro caso
# Lo representamos como diccionario: (d1, d2, suma) -> probabilidad
factor_suma = {}                              # diccionario vacío para llenar
for d1 in range(1, 7):                        # recorre cada valor posible de D1
    for d2 in range(1, 7):                    # recorre cada valor posible de D2
        s = d1 + d2                           # calcula la suma exacta
        factor_suma[(d1, d2, s)] = 1.0        # esa combinación ocurre con prob 1
 
 
# Eliminación de Variables 
# Queremos P(Suma). Para eso eliminamos D1 y D2.
# La idea: en vez de trabajar con las 3 variables juntas,
# vamos "absorbiendo" variables de una en una.
 
# Paso 4: combinar P(D1) con P(Suma | D1, D2)
# Multiplicamos ambos factores para obtener un factor conjunto
# que representa P(D1) * P(Suma | D1, D2), con variables (D1, D2, Suma)
factor_d1_suma = {}                           # nuevo factor a construir
for (d1, d2, s), p_cond in factor_suma.items(): # recorre cada entrada del factor suma
    p_d1 = factor_d1[d1]                     # busca P(D1=d1)
    factor_d1_suma[(d1, d2, s)] = p_d1 * p_cond  # multiplica ambas probabilidades
 
# Paso 5: eliminar D1 sumando sobre todos sus valores
# Resultado: un factor que ya no contiene D1, solo (D2, Suma)
factor_d2_suma = {}                           # factor reducido sin D1
for (d1, d2, s), p in factor_d1_suma.items(): # recorre el factor combinado
    clave = (d2, s)                           # nueva clave sin D1
    factor_d2_suma[clave] = factor_d2_suma.get(clave, 0) + p  # acumula sumando sobre D1
 
# Paso 6: combinar el resultado con P(D2)
# Multiplicamos por P(D2) para incluir su probabilidad
factor_con_d2 = {}                            # factor con P(D2) incluida
for (d2, s), p in factor_d2_suma.items():    # recorre el factor (D2, Suma)
    p_d2 = factor_d2[d2]                     # busca P(D2=d2)
    factor_con_d2[(d2, s)] = p * p_d2        # multiplica
 
# Paso 7: eliminar D2 sumando sobre todos sus valores
# Resultado final: P(Suma) — ya sin D1 ni D2
factor_suma_final = {}                        # factor final solo con Suma
for (d2, s), p in factor_con_d2.items():     # recorre el factor (D2, Suma)
    factor_suma_final[s] = factor_suma_final.get(s, 0) + p  # acumula sumando sobre D2
 
 
# ── Resultados ──────────────────────────────────────────
print("P(Suma) calculada por Eliminación de Variables:")
print(f"{'Suma':>6} | {'Probabilidad':>12} | {'Porcentaje':>10}")
print("-" * 35)
for s in sorted(factor_suma_final):          # recorre sumas del 2 al 12
    p = factor_suma_final[s]                 # obtiene la probabilidad de esa suma
    print(f"{s:>6} | {p:>12.6f} | {p*100:>9.2f}%")  # imprime formateado
 
# Verificación: todas las probabilidades deben sumar 1
total = sum(factor_suma_final.values())      # suma todas las probabilidades
print(f"\nSuma total de probabilidades: {total:.6f}  (debe ser 1.0)")
 