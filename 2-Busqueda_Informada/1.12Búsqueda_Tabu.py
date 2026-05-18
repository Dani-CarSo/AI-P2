#12
#Búsqueda Tabú

from random import randint  


def tabu_search(objetos, capacidad_maxima, tamano_tabu, num_iteraciones):

    def evaluar_solucion(solucion):
        valor_total = sum(objetos[i][0] for i in range(len(solucion)) if solucion[i])  
        peso_total = sum(objetos[i][1] for i in range(len(solucion)) if solucion[i])   
        if peso_total > capacidad_maxima:
            return 0
        return valor_total

    def generar_vecino(solucion):  
        vecindario = []
        for i in range(len(solucion)):
            if not solucion[i]:
                for j in range(len(solucion)):
                    if solucion[j]:
                        vecino = solucion.copy()
                        vecino[i] = 1
                        vecino[j] = 0
                        vecindario.append(vecino)
        return vecindario

    mejor_solucion = [0] * len(objetos)  
    mejor_valor = 0

    solucion_actual = [randint(0, 1) for _ in range(len(objetos))]  

    lista_tabu = []

    for _ in range(num_iteraciones): 
        vecindario = generar_vecino(solucion_actual)
        vecindario_no_tabu = [vecino for vecino in vecindario if vecino not in lista_tabu]
        if not vecindario_no_tabu:
            break

        mejor_vecino = max(vecindario_no_tabu, key=evaluar_solucion)
        valor_vecino = evaluar_solucion(mejor_vecino)

        if valor_vecino > mejor_valor:
            mejor_solucion = mejor_vecino
            mejor_valor = valor_vecino

        solucion_actual = mejor_vecino
        valor_actual = valor_vecino  
        lista_tabu.append(solucion_actual)
        if len(lista_tabu) > tamano_tabu:
            lista_tabu.pop(0)

    return mejor_solucion, mejor_valor  

