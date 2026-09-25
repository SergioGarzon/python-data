'''
Habitación de un hotel
Crear una clase Habitacion con número, cantidad máxima de personas, precio por noche y estado de ocupación.
Implementar el constructor y __str__(). Agregar métodos que permitan ocupar y liberar la habitación. Una habitación
ocupada no puede volver a ocuparse hasta que sea liberada.
'''

from Clases_Exercises.Exercise_clases_4.Habitacion import Habitacion

habitacion_1 = Habitacion(150, 4, 5505.55, "ocupada")

print(habitacion_1)

