class Surtidor:
    
    def __init__(self, nro_surtidor, cantidad, tipo):
        self.nro_surtidor = nro_surtidor
        self.cantidad = cantidad
        self.tipo = tipo
        
    def get_nro_superior(self):
        return self.nro_surtidor
    
    def get_cantidad(self):
        return self.cantidad

    def get_tipo(self):
        return self.tipo
    
    def to_string(self):
        return "{ Numero de surtidor: " + str(self.nro_surtidor) + ", cantidad: " + str(self.cantidad) + ", tipo: " + str(self.tipo) + " }"
    