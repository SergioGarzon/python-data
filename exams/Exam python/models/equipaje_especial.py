# **Equipaje Especial**: mismo importe que el equipaje común con un recargo de $1.500
# por kg transportado

from models.equipaje import Equipaje

class EquipajeEspecial(Equipaje):
    
    importe_final = None
    
    # Constructor
    
    def __init__(self, codigo_identificacion, propietario, destino, peso, tarifa_base):
        super().__init__(codigo_identificacion, propietario, destino, peso, tarifa_base)
    
    # Calculamos el importe final
    
    def importe(self):
        if(int(super().peso()) > 0):
            importe_final = super().tarifa_base() + (super().peso * 1500)
        else:
            importe_final = super().tarifa_base()
    
        return importe_final
            
    # toString
        
    def __str__(self):
        return super().__str__()
            
    
        
    
    
    