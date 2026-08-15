class Surtidor:
    
    def __init__(self, nro_surtidor, cantidad, tipo):
        self.nro_surtidor = nro_surtidor
        self.cantidad = cantidad
        self.tipo = tipo
        
    def to_string(self):
        return "Numero de surtidor: " + str(self.nro_surtidor)