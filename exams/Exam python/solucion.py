from models.equipaje import Equipaje
from models.equipaje_especial import EquipajeEspecial
from models.equipaje_comun import EquipajeComun

# Para los linters que marcan como clases no usadas
__all__ = ["Equipaje", "EquipajeComun", "EquipajeEspecial"]

class Solucion:
    
    def __init__(self):
        self.equipajes = []
        
    def agregar(self, equipaje):
        self.equipajes.add(equipaje)