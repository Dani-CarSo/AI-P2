#69
#k-NN, k-Medias y Clustering

import numpy as np
# Librería para operaciones numéricas

from collections import Counter
# Se usa para contar votos en k-NN

# -----------------------------
# GENERACIÓN DE DATOS
# -----------------------------

np.random.seed(42)
# Fija semilla para reproducibilidad

# Clase A (grupo 0)
class_A = np.random.normal([2, 2], 0.6, (40, 2))
# 40 puntos alrededor de (2,2)

# Clase B (grupo 1)
class_B = np.random.normal([8, 8], 0.6, (40, 2))
# 40 puntos alrededor de (8,8)

# Etiquetas (solo para k-NN)
labels_A = np.zeros(len(class_A))
# Clase 0

labels_B = np.ones(len(class_B))
# Clase 1

# Dataset supervisado (k-NN usa etiquetas)
X = np.vstack((class_A, class_B))
# Datos

y = np.hstack((labels_A, labels_B))
# Etiquetas

# Dataset no supervisado (K-Means no usa etiquetas)
X_unsupervised = X.copy()
# Copia de datos sin etiquetas

# -----------------------------
# k-NN (SUPERVISADO)
# -----------------------------

def knn_predict(point, X, y, k=3):
    # Predice la clase de un punto
    
    distances = np.linalg.norm(X - point, axis=1)
    # Distancia entre el punto y todos los datos
    
    nearest_indices = np.argsort(distances)[:k]
    # Índices de los k vecinos más cercanos
    
    nearest_labels = y[nearest_indices]
    # Etiquetas de esos vecinos
    
    vote = Counter(nearest_labels).most_common(1)[0][0]
    # Voto mayoritario
    
    return vote
    # Regresa clase predicha

# -----------------------------
# K-MEANS (NO SUPERVISADO)
# -----------------------------

K = 2
# Número de clusters

centroids = X_unsupervised[np.random.choice(len(X_unsupervised), K, replace=False)]
# Centroides iniciales aleatorios

def assign_clusters(data, centroids):
    # Asigna puntos a clusters
    
    clusters = []
    # Lista de asignaciones

    for point in data:
        # Recorre cada punto
        
        distances = np.linalg.norm(point - centroids, axis=1)
        # Distancia a cada centroide
        
        clusters.append(np.argmin(distances))
        # Asigna al cluster más cercano

    return np.array(clusters)
    # Devuelve clusters

def update_centroids(data, clusters, K):
    # Recalcula centros
    
    new_centroids = []
    # Lista de nuevos centroides

    for k in range(K):
        # Para cada cluster
        
        points = data[clusters == k]
        # Puntos del cluster
        
        new_centroids.append(points.mean(axis=0))
        # Centroide = promedio

    return np.array(new_centroids)
    # Regresa nuevos centros

# -----------------------------
# INTERACCIÓN
# -----------------------------

print("=== k-NN + K-MEANS INTERACTIVO ===")
print("Opciones:")
print("1 → k-NN (clasificación)")
print("2 → K-Means (clustering)")
print("3 → probar punto manual")
print("4 → salir\n")

while True:
    option = input("Elige opción: ")
    # Menú interactivo

    if option == "4":
        # Salir
        break

    # -------------------------
    # k-NN interactivo
    # -------------------------
    if option == "1":
        x = float(input("x: "))
        y_point = float(input("y: "))
        # Usuario ingresa punto

        point = np.array([x, y_point])
        # Convierte a vector

        prediction = knn_predict(point, X, y)
        # Predicción k-NN

        print(f"Clase predicha (k-NN): {prediction}")
        # Muestra resultado

    # -------------------------
    # K-MEANS interactivo
    # -------------------------
    elif option == "2":
        clusters = assign_clusters(X_unsupervised, centroids)
        # Asignación de clusters

        new_centroids = update_centroids(X_unsupervised, clusters, K)
        # Recalcular centroides

        shift = np.linalg.norm(new_centroids - centroids)
        # Cambio en centroides

        centroids = new_centroids
        # Actualizar

        print("Centroides actuales:")
        print(centroids)
        # Mostrar clusters

        print(f"Cambio: {shift:.4f}")
        # Mostrar convergencia

    # -------------------------
    # Probar punto sin decidir método
    # -------------------------
    elif option == "3":
        x = float(input("x: "))
        y_point = float(input("y: "))
        # Entrada usuario

        point = np.array([x, y_point])
        # Vector

        print("k-NN:", knn_predict(point, X, y))
        # Clasificación supervisada

        distances = np.linalg.norm(centroids - point, axis=1)
        # Distancia a clusters

        print("Cluster más cercano (K-Means):", np.argmin(distances))
        # Clustering no supervisado

    else:
        print("Opción inválida")
        # Manejo de error