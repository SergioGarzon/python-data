# - **Equipaje Común**: importe final igual a la tarifa base

from models.equipaje import Equipaje

class EquipajeComun(Equipaje):
    
    importe_final = None

    # Constructor

    def __init__(self, codigo_identificacion, propietario, destino, peso, tarifa_base):
        super().__init__(codigo_identificacion, propietario, destino, peso, tarifa_base)
        
    # Calculamos el importe final
        
    def importe(self):
        return float(self.tarifa_base)
        
    # toString
    
    def __str__(self):
        return "Equipaje comun ( " + super().__str__() + " )"
        
    
