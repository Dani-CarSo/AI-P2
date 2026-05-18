#30
# MDP Parcialmente Observable (POMDP)

import random
# Importa la librería random para generar números aleatorios
# Estados posibles
estados = list(range(1, 11))
# Crea una lista de números del 1 al 10 → posibles valores del número oculto

# Número real (oculto)
numero_real = random.choice(estados)
# Elige aleatoriamente uno de los estados → este es el número verdadero (no lo ves)

# Creencia inicial uniforme (todas las probabilidades iguales)
belief = {s: 1/len(estados) for s in estados}
# Crea un diccionario donde:
# cada número tiene la misma probabilidad (0.1)
# Ejemplo: {1:0.1, 2:0.1, ..., 10:0.1}


def observar(intento, real):
    # Función que genera una observación (pista)
    # intento = número que dices
    # real = número verdadero

    # Observación con ruido (30% error)
    if intento == real:
        return "correcto"
        # Si adivinaste exactamente, devuelve "correcto"
    
    if intento < real:
        pista = "mayor"
        # Si tu número es menor al real → debería decir "mayor"
    else:
        pista = "menor"
        # Si tu número es mayor al real → debería decir "menor"
    
    # ruido
    if random.random() < 0.3:
        # Genera un número entre 0 y 1
        # Si es menor a 0.3 → 30% de probabilidad de error
        
        pista = "mayor" if pista == "menor" else "menor"
        # Invierte la pista → miente
    
    return pista
    # Regresa la pista (puede ser correcta o falsa)


def actualizar_belief(belief, intento, obs):
    # Función que actualiza la creencia usando probabilidad (Bayes)
    # belief = probabilidades actuales
    # intento = número que elegiste
    # obs = observación recibida

    nuevo = {}
    # Diccionario para guardar las nuevas probabilidades
    
    for s in belief:
        # Recorre cada posible estado (cada número posible)
        
        # Probabilidad de observar obs dado estado s
        if intento == s:
            prob_obs = 1.0 if obs == "correcto" else 0.0
            # Si el número real fuera s:
            # solo puede decir "correcto"
        
        elif intento < s:
            # debería decir "mayor"
            prob_obs = 0.7 if obs == "mayor" else 0.3
            # 70% dice la verdad, 30% miente
        
        else:
            # debería decir "menor"
            prob_obs = 0.7 if obs == "menor" else 0.3
            # igual: 70% correcto, 30% error
        
        nuevo[s] = belief[s] * prob_obs
        # Fórmula de Bayes (sin normalizar):
        # nueva probabilidad = creencia previa * probabilidad de observación
    
    # normalizar
    total = sum(nuevo.values())
    # Suma todas las probabilidades
    
    if total > 0:
        # Evita división entre cero
        
        for s in nuevo:
            nuevo[s] /= total
            # Divide cada valor entre la suma total
            # → asegura que todas sumen 1
    
    return nuevo
    # Regresa la nueva creencia actualizada


print(" Adivina el número (1-10)")
# Mensaje inicial

print("El sistema mantiene probabilidades\n")
# Explica que se usan probabilidades internas


while True:
    # Bucle infinito → el juego sigue hasta acertar
    
    print("\nCreencia actual:")
    # Muestra las probabilidades actuales
    
    for s in estados:
        print(f"{s}: {belief[s]:.2f}", end=" | ")
        # Imprime cada número con su probabilidad (2 decimales)
    
    print()
    # Salto de línea
    
    intento = int(input("\nTu intento: "))
    # Pide al usuario un número
    
    obs = observar(intento, numero_real)
    # Genera la observación (puede mentir)
    
    print(" Observación:", obs)
    # Muestra la pista
    
    if obs == "correcto":
        print("¡Correcto!")
        # Si acertaste, mensaje
        
        break
        # Termina el juego
    
    # actualizar creencia (Bayes)
    belief = actualizar_belief(belief, intento, obs)
    # Actualiza las probabilidades usando la observación