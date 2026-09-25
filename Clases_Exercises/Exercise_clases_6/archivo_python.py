'''
Cuenta de puntos de un cliente
Crear una clase Cliente con número, nombre y cantidad de puntos acumulados. Implementar el constructor y
__str__(). Agregar métodos sumar_puntos(cantidad) y canjear_puntos(cantidad). No se deben aceptar cantidades
negativas ni permitir un canje superior a los puntos disponibles. Crear dos clientes y realizar distintas operaciones

Voy a hacer una herencia, que Cliente herede de Persona

'''

from client import Client

cliente_1 = Client(54330, "Sergio", 100)
cliente_2 = Client(52127, "Pablo", 55)

print(cliente_1)
print(cliente_2)

