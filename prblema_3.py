#---------------------------------------------------------------------
#Alejandro Alfosnso Rodriguez Zunñiga
#Curso:Fundamentos de programacion
#Grupo: 213022A_2201
#Problema 3: Control de inventario y reabastecimiento de artículos
#Autor: Alejandro Alfosnso Rodriguez Zunñiga
#---------------------------------------------------------------------


#matriz de inventario con codigo nombre cantidad estock minimo y stcok actual 
# donde M001 es el codigo del producto, Mouse es el nombre del producto, 15 es el stock actual y 25 es el stock minimo


lista_inventario = [
["M001", "Mouse", 15, 5],
["M002", "Teclado", 10, 8],
["M003", "Monitor", 10, 20],
["M004", "Impresora", 20, 15],
["M005", "Silla de oficina",10, 25],
["M006", "Escritorio", 8, 15]
]



#Funcion paea calcular el pedido de reabastecimiento
# Esta función recibe:
# - stock actual
# - stock mínimo
#
# La función compara ambos valores:
# Si el stock actual es menor al mínimo,
# calcula cuánto hace falta pedir.
#
# Si el stock es suficiente,
# devuelve 0.

def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
        return cantidad_a_pedir
    else:
        return 0
    
    
for producto in lista_inventario:
        
    codigo = producto[0]
    nombre = producto[1]
    stock_actual = producto[2]
    stock_minimo = producto[3]
    
    
# Llamar la función para calcular cuánto pedir
    
    cantidad = calcular_pedido(stock_actual, stock_minimo)
        
        
        
# imprimimos el resultado para cada producto
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad)
    print("---------------------------")