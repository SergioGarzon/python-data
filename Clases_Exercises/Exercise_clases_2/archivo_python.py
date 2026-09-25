'''
Libro de una biblioteca
Crear una clase Libro con título, autor, cantidad de páginas y estado de préstamo. 
Implementar el constructor y __str__(). Agregar los métodos prestar() y devolver(). 
No debe ser posible prestar un libro que ya se encuentra prestado. 
Crear un libro y realizar algunas operaciones para comprobar su funcionamiento
'''

from Clases_Exercises.Exercise_clases_2.Libro import Libro

libro_1 = Libro("El señor de los anillos", "JRR Tolkien", 550, "devuelto")

print(libro_1)

