# **Equipaje Especial**: mismo importe que el equipaje común con un recargo de $1.500
# por kg transportado

from models.equipaje import Equipaje

class EquipajeEspecial(Equipaje):
        
    # Constructor
    
    def __init__(self, codigo_identificacion, propietario, destino, peso, tarifa_base):
        super().__init__(codigo_identificacion, propietario, destino, peso, tarifa_base)
    
    # Calculamos el importe final
    
    def importe(self):
        
        importe_final = 0.0
        
        if int(self.peso) > 0:
            importe_final = float(self.tarifa_base) + (int(self.peso) * 1500)
        else:
            importe_final = float(self.tarifa_base)
                
        return importe_final
            
    # toString
        
    def __str__(self):
        return "Equipaje especial ( " + super().__str__() + " ) "
            
    
        
    
    
    