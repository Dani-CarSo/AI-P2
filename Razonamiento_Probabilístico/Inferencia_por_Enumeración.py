#53
#Inferencia por Enumeración

P_robo = 0.001        # hay 0.1% de probabilidad de que haya un robo
P_terremoto = 0.002   # hay 0.2% de probabilidad de que haya un terremoto

# Probabilidad de que suene la alarma dado si hubo robo y/o terremoto
# La clave es una tupla (robo, terremoto), ambos pueden ser True o False
P_alarma = {
    (True,  True):  0.95,   # robo Y terremoto  → alarma suena el 95% del tiempo
    (True,  False): 0.94,   # solo robo          → alarma suena el 94% del tiempo
    (False, True):  0.29,   # solo terremoto     → alarma suena el 29% del tiempo
    (False, False): 0.001,  # ninguno            → alarma suena el 0.1% (falla)
}

# Probabilidad de que Juan llame dado si la alarma está activa (True) o no (False)
P_juan  = {True: 0.90, False: 0.05}  # si alarma=True llama 90%, si False solo 5%

# Probabilidad de que María llame dado si la alarma está activa o no
P_maria = {True: 0.70, False: 0.01}  # si alarma=True llama 70%, si False solo 1%


def prob_conjunta(robo, terremoto, alarma, juan, maria):
    # Calcula la probabilidad de UNA combinación específica de todas las variables
    # Es el producto de cada variable condicionada a sus padres en la red

    return (
        # P(Robo): si robo=True usamos P_robo, si False usamos su complemento
        (P_robo if robo else 1 - P_robo) *

        # P(Terremoto): igual, si es True usamos P_terremoto, si no su complemento
        (P_terremoto if terremoto else 1 - P_terremoto) *

        # P(Alarma | Robo, Terremoto): buscamos en el diccionario según (robo, terremoto)
        (P_alarma[(robo, terremoto)] if alarma else 1 - P_alarma[(robo, terremoto)]) *

        # P(Juan | Alarma): si juan=True usamos la prob de llamar, si no su complemento
        (P_juan[alarma] if juan else 1 - P_juan[alarma]) *

        # P(Maria | Alarma): igual que Juan pero con los valores de María
        (P_maria[alarma] if maria else 1 - P_maria[alarma])
    )


def inferencia_enumeracion(juan_obs, maria_obs):
    # juan_obs y maria_obs son la evidencia: lo que sabemos que ocurrió

    resultado = {}  # aquí guardaremos la probabilidad sin normalizar de cada valor de Robo

    for robo in [True, False]:          # probamos robo=True y robo=False (la variable consulta)
        total = 0.0                     # acumulador: suma de todas las combinaciones ocultas
        for terremoto in [True, False]: # enumeramos terremoto (variable oculta)
            for alarma in [True, False]:# enumeramos alarma    (variable oculta)
                # sumamos la prob conjunta fijando juan y maria a la evidencia observada
                total += prob_conjunta(robo, terremoto, alarma, juan_obs, maria_obs)
        resultado[robo] = total         # guardamos la suma para este valor de robo

    # Normalizar: dividimos cada valor entre la suma total para que sumen 1
    suma = resultado[True] + resultado[False]        # suma total (factor de normalización α)
    return {k: v / suma for k, v in resultado.items()} # devuelve {True: prob, False: prob}


# --- Punto de entrada ---
evidencia = {"JuanLlama": True, "MariaLlama": True}  # lo que observamos

# Llamamos a la inferencia pasando la evidencia
P = inferencia_enumeracion(evidencia["JuanLlama"], evidencia["MariaLlama"])

print(f"Evidencia: {evidencia}")
print(f"P(Robo=True  | evidencia) = {P[True]:.6f}")   # prob de que SÍ hubo robo
print(f"P(Robo=False | evidencia) = {P[False]:.6f}")  # prob de que NO hubo robo