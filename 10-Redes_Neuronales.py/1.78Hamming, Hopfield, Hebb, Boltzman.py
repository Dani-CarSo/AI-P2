#78
#Hamming, Hopfield, Hebb, Boltzmann

import numpy as np    # Importamos numpy para manejo de vectores y matrices
import math           # Para funciones matemáticas como exp() en Boltzmann
import random         # Para la naturaleza estocástica (azar) de Boltzmann

def ejecutar_laboratorio():
    # --- ENTRADA DE DATOS ---
    print("--- INICIO DEL PROCESO ---")
    # Pedimos al usuario una cadena como "1,-1,1" y la limpiamos
    entrada = input("Introduce 3 valores (1 o -1) separados por coma: ")
    # Convertimos el texto en una lista de enteros
    lista = [int(x.strip()) for x in entrada.split(",")]
    # Lo transformamos en un vector de Numpy para cálculos matemáticos
    patron = np.array(lista)

    # --- 1. REGLA DE HEBB (Aprendizaje por asociación) ---
    # La teoría dice que el peso w es el producto de la entrada por la salida
    salida_deseada = 1 # Definimos que este patrón debe dar una respuesta positiva
    w_hebb = patron * salida_deseada # Multiplicación elemento a elemento
    print(f"Pesos de Hebb: {w_hebb} (Representan la 'memoria' del patrón)")

    # --- 2. RED DE HOPFIELD (Recuperación de memoria) ---
    # Creamos una matriz de pesos 'M' multiplicando el patrón por sí mismo traspuesto
    matriz_W = np.outer(patron, patron) 
    # La diagonal se hace cero porque una neurona no debe retroalimentarse a sí misma
    np.fill_diagonal(matriz_W, 0)
    
    # Creamos una versión con 'ruido' invirtiendo el primer valor
    ruido = patron.copy()
    ruido[0] = ruido[0] * -1 
    # Intentamos recuperar el original: signo de (Matriz por vector con ruido)
    recuperado = np.sign(np.dot(matriz_W, ruido))
    print(f"Hopfield recuperó {recuperado} a partir de {ruido}")

    # --- 3. RED DE HAMMING (Clasificación por similitud) ---
    # Definimos dos "moldes" o prototipos fijos
    prototipos = np.array([[1, 1, 1], [-1, -1, -1]])
    # Multiplicamos los moldes por tu entrada para ver cuánto "encajan"
    # Se suma N/2 (1.5) para normalizar el resultado
    activacion = np.dot(prototipos, patron) + 1.5
    # np.argmax nos dice cuál de los dos resultados fue el más alto
    ganador = np.argmax(activacion)
    print(f"Hamming dice: Tu patrón se parece más al grupo {ganador}")

    # --- 4. MÁQUINA DE BOLTZMANN (Decisión con probabilidad) ---
    # Pedimos la temperatura: 0.1 es casi determinista, 10 es puro azar
    T = float(input("Temperatura (0.1 - 10): "))
    # Calculamos el potencial (suma ponderada de entrada y pesos)
    u = np.dot(w_hebb, patron)
    # Aplicamos la función logística para obtener una probabilidad entre 0 y 1
    probabilidad = 1 / (1 + math.exp(-u / T))
    # Tiramos un dado virtual: si el azar es menor a la probabilidad, se activa (1)
    resultado = 1 if random.random() < probabilidad else -1
    print(f"Boltzmann decidió {resultado} con una probabilidad de {probabilidad:.2%}")

ejecutar_laboratorio()