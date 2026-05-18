#67
#Algoritmo EM


import numpy as np
# Librería para cálculos numéricos

# Datos simulados (sin etiquetas)
np.random.seed(42)
# Fija semilla para reproducibilidad

data1 = np.random.normal(0, 1, 50)
# Grupo oculto 1

data2 = np.random.normal(5, 1, 50)
# Grupo oculto 2

data = np.hstack((data1, data2))
# Une los datos

np.random.shuffle(data)
# Mezcla los datos (como en la vida real)


# Inicialización
mu1, mu2 = 1.0, 4.0
# Medias iniciales (mal estimadas a propósito)

sigma1, sigma2 = 1.0, 1.0
# Desviaciones iniciales

pi1, pi2 = 0.5, 0.5
# Probabilidades iniciales de pertenencia


# Función gaussiana
def gaussian(x, mu, sigma):
    # Distribución normal
    
    return (1 / (np.sqrt(2*np.pi)*sigma)) * np.exp(-((x-mu)**2)/(2*sigma**2))
    # Fórmula de probabilidad


# Paso EM (E-step + M-step)
def em_step():
    global mu1, mu2, sigma1, sigma2, pi1, pi2
    
    gamma1 = []
    gamma2 = []
    # Responsabilidades (probabilidades de pertenencia)


    # E-step
    for x in data:
        # Recorre cada punto
        
        p1 = pi1 * gaussian(x, mu1, sigma1)
        # Probabilidad de grupo 1
        
        p2 = pi2 * gaussian(x, mu2, sigma2)
        # Probabilidad de grupo 2
        
        total = p1 + p2
        # Normalización
        
        gamma1.append(p1 / total)
        # Probabilidad de pertenecer a grupo 1
        
        gamma2.append(p2 / total)
        # Probabilidad de pertenecer a grupo 2

    gamma1 = np.array(gamma1)
    gamma2 = np.array(gamma2)


    # M-step
    mu1 = np.sum(gamma1 * data) / np.sum(gamma1)
    # Nueva media grupo 1
    
    mu2 = np.sum(gamma2 * data) / np.sum(gamma2)
    # Nueva media grupo 2

    sigma1 = np.sqrt(np.sum(gamma1 * (data - mu1)**2) / np.sum(gamma1))
    # Nueva varianza grupo 1

    sigma2 = np.sqrt(np.sum(gamma2 * (data - mu2)**2) / np.sum(gamma2))
    # Nueva varianza grupo 2

    pi1 = np.mean(gamma1)
    # Proporción grupo 1

    pi2 = np.mean(gamma2)
    # Proporción grupo 2

   
    # Mostrar estado
    print("\n--- Estado actual EM ---")
    print(f"mu1 = {mu1:.3f}, mu2 = {mu2:.3f}")
    print(f"sigma1 = {sigma1:.3f}, sigma2 = {sigma2:.3f}")
    print(f"pi1 = {pi1:.3f}, pi2 = {pi2:.3f}")
    print("-" * 40)

# Interacción con usuario
print("=== EM INTERACTIVO ===")
print("Presiona ENTER para hacer una iteración")
print("Escribe 'salir' para terminar\n")

iter_count = 0

while True:
    user_input = input("Iterar EM → ")
    # Espera input del usuario

    if user_input.lower() == "salir":
        # Salida del programa
        break

    iter_count += 1
    print(f"\nIteración {iter_count}")
    # Muestra número de iteración

    em_step()
    # Ejecuta un paso EM (E-step + M-step)