from person import Person

class Client(Person):
    
    numero = None
    cantidad_puntos = None
    
    def __init__(self, numero, nombre, cantidad_puntos):
        self.numero = numero
        super().__init__(nombre)
        self.cantidad_puntos = cantidad_puntos
        
    def sumar_puntos(self, cantidad):
        if(cantidad > 0):
            self.cantidad_puntos += cantidad 

    def canjear_puntos(self, cantidad):
        if(cantidad <= self.cantidad_puntos):
            self.cantidad_puntos -= cantidad
        
    def __str__(self):
        return (f"Numero: {self.numero}, nombre: {super().__str__()}, cantidad de puntos: {self.cantidad_puntos}")
    