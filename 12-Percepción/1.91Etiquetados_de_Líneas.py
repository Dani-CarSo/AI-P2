#91
#Etiquetados de Líneas

# Definimos una lista de diccionarios que representan ventas de productos
ventas = [
    {"producto": "Libreta", "precio": 12.50, "cantidad": 4},
    {"producto": "Pluma", "precio": 2.10, "cantidad": 10},
    {"producto": "Mochila", "precio": 45.00, "cantidad": 1}
]

total_general = 0  # Inicializamos un acumulador para el total de todas las ventas

# Iniciamos un bucle para recorrer cada diccionario dentro de la lista 'ventas'
for venta in ventas:
    # Calculamos el subtotal multiplicando el precio por la cantidad
    subtotal = venta["precio"] * venta["cantidad"]
    
    # Sumamos el subtotal actual al acumulador total_general
    total_general += subtotal
    
    # Imprimimos un reporte formateado usando f-strings para cada artículo
    print(f"Producto: {venta['producto']} | Subtotal: ${subtotal:.2f}")

# Al finalizar el bucle, mostramos el resultado final de la operación
print("-" * 30)  # Imprime una línea separadora visual
print(f"El total recaudado es: ${total_general:.2f}")