# Cada vez que se le realiza un mantenimiento se registra el nombre 
# del operario que lo realiza, la fecha en que se efectuó y el importe 
# que se gastó en repuestos.

from abc import ABC, abstractmethod

class Mantenimiento(ABC):
    
    _operario = None
    _fecha = None
    _importe_repuestos = None
    
    # Constructor
        
    def __init__(self, operario, fecha, importe_repuestos):
        self._operario = operario
        self._fecha = fecha
        self._importe_repuestos = importe_repuestos
        
    # Getters
    
    @property
    def operario(self):
        return self._operario

    @property
    def fecha(self):
        return self._fecha
    
    @property
    def importe_repuestos(self):
        return self._importe_repuestos
    
    # Setters
    
    @operario.setter
    def operario(self, operario):
        self._operario = operario
    
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha
    
    @importe_repuestos.setter
    def importe_repuestos(self, importe_repuestos):
        self._importe_repuestos = importe_repuestos
        
    
    # Metodo abstracto para calcular el gasto total
    @abstractmethod
    def gasto_total(self):
        pass        
    
    # toString
    
    def __str__(self):
        return f"Mantenimiento ( Nombre operario: {self._operario}, fecha: {self._fecha}, importe repuestos: {self._importe_repuestos})"
     