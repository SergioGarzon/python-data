# nombre, especie, edad y peso

class Mascota:
    
    nombre = None
    especie = None
    edad = None
    peso = None
    
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso            
    
    def peso(self, nuevo_peso):
        if(nuevo_peso > 0):
            self.peso = nuevo_peso
            
    def es_adulta(self):
        return self.edad > 2
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {str(self.edad)}, Peso: {self.peso}"