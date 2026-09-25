# número, cantidad máxima de personas, precio por noche y estado de ocupación

class Habitacion:
    
    def __init__(self, numero, cant_max_personas, precio_noche, estado_ocupacion):
            self.numero = numero
            self.cant_max_personas = cant_max_personas
            self.precio_noche = precio_noche
            self.estado_ocupacion = estado_ocupacion
            
    def ocupar(self):
        if self.estado_ocupacion != "ocupada":
            self.estado_ocupacion = "ocupada"
       
    def liberar(self):
        if self.estado_ocupacion != "liberar":
            self.estado_ocupacion = "liberar"
                
    def __str__(self):
        return (
            "{ Numero: " + str(self.numero) + 
            ", cantidad maxima de personas: " + str(self.cant_max_personas) + 
            ", precio de la noche: " + str(self.precio_noche) + 
            ", estado de ocupacion: " + str(self.estado_ocupacion) +
            " }"
        )