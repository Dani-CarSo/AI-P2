#68
#Agrupamiento NO supervisado

import numpy as np

np.random.seed(42)
# Fija semilla para que los resultados sean reproducibles

# Grupo 1 de datos (cluster 1)
cluster1 = np.random.normal([2, 2], 0.5, (50, 2))
# 50 puntos alrededor de (2,2)

# Grupo 2 de datos (cluster 2)
cluster2 = np.random.normal([8, 8], 0.5, (50, 2))
# 50 puntos alrededor de (8,8)

# Grupo 3 de datos (cluster 3)
cluster3 = np.random.normal([2, 8], 0.5, (50, 2))
# 50 puntos alrededor de (2,8)

# Unimos todos los datos en un solo conjunto
data = np.vstack((cluster1, cluster2, cluster3))
# Ahora tenemos datos sin etiquetas (no supervisado)

# -----------------------------
# Inicialización de K-Means
# -----------------------------

K = 3
# Número de clusters que queremos encontrar

centroids = data[np.random.choice(len(data), K, replace=False)]
# Elegimos K puntos aleatorios como centroides iniciales

# -----------------------------
# Función de asignación de clusters
# -----------------------------

def assign_clusters(data, centroids):
    # Asigna cada punto al centroide más cercano
    
    clusters = []
    # Lista donde guardamos el cluster asignado a cada punto

    for point in data:
        # Recorre cada punto del dataset
        
        distances = np.linalg.norm(point - centroids, axis=1)
        # Calcula distancia del punto a cada centroide
        
        cluster = np.argmin(distances)
        # Elige el centroide más cercano
        
        clusters.append(cluster)
        # Guarda asignación

    return np.array(clusters)
    # Regresa array con asignaciones

# -----------------------------
# Función de actualización de centroides
# -----------------------------

def update_centroids(data, clusters, K):
    # Recalcula centroides como promedio de cada grupo
    
    new_centroids = []
    # Lista de nuevos centroides

    for k in range(K):
        # Para cada cluster
        
        points = data[clusters == k]
        # Obtiene puntos asignados a ese cluster
        
        centroid = points.mean(axis=0)
        # Calcula el centro (media)
        
        new_centroids.append(centroid)
        # Guarda nuevo centroide

    return np.array(new_centroids)
    # Regresa nuevos centroides

# -----------------------------
# Interfaz interactiva
# -----------------------------

print("=== K-MEANS INTERACTIVO ===")
print("Presiona ENTER para una iteración")
print("Escribe 'salir' para terminar\n")

iteration = 0
# Contador de iteraciones

# -----------------------------
# Loop principal
# -----------------------------

while True:
    # Bucle infinito controlado por usuario

    user_input = input("Iterar K-Means → ")
    # Espera acción del usuario

    if user_input.lower() == "salir":
        # Salida del programa
        break

    iteration += 1
    # Incrementa iteración

    print(f"\n--- Iteración {iteration} ---")

    # -------------------------
    # Paso 1: asignación
    # -------------------------
    clusters = assign_clusters(data, centroids)
    # Cada punto se asigna a su centroide más cercano

    # -------------------------
    # Paso 2: actualización
    # -------------------------
    new_centroids = update_centroids(data, clusters, K)
    # Se recalculan los centroides

    # -------------------------
    # Verificar convergencia
    # -------------------------
    shift = np.linalg.norm(new_centroids - centroids)
    # Calcula cuánto se movieron los centroides

    centroids = new_centroids
    # Actualiza centroides

    # -------------------------
    # Mostrar resultados
    # -------------------------
    print(f"Cambio en centroides: {shift:.4f}")
    # Muestra cuánto cambiaron

    print("Centroides actuales:")
    print(centroids)
    # Muestra posiciones de los clusters

    print("-" * 40)