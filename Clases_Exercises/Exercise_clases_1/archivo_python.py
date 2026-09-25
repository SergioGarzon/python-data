'''
Producto de una tienda
Crear una clase Producto que permita almacenar código, descripción, precio y stock. 
Implementar el constructor y __str__(). 

Agregar un método hay_stock() que indique si existen unidades disponibles y un método valor_stock() que
calcule el valor total de las unidades almacenadas. Crear dos productos y mostrar sus datos
'''

from Clases_Exercises.Exercise_clases_1.Producto import Producto

prod_1 = Producto(1, "Producto 1", 1235.5, 0)
prod_2 = Producto(2, "Producto 2", 8787.66, 1)

print("Producto 1")
print(prod_1)
print("Hay stock" if prod_1.hay_stock() else "No hay stock")
print("Valor del producto: " + str(prod_1.valor_stock()))

print("\nProducto 2")
print(prod_2)
print("Hay stock" if prod_2.hay_stock() else "No hay stock")
print("Valor del producto: " + str(prod_2.valor_stock()))


