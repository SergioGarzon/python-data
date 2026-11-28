from models.Mantenimiento import Mantenimiento

class Correctivo(Mantenimiento):
    
    _horas_parada = None
    _importe_tecnico = None
    
    # Constructor
    
    def __init__(self, operario, fecha, importe_repuestos, horas_parada, importe_tecnico):
        super().__init__(operario, fecha, importe_repuestos)
        self._horas_parada = horas_parada
        self._importe_tecnico = importe_tecnico
        
    # Getters
    
    @property
    def horas_parada(self):
        return self._horas_parada
    
    @property
    def importe_tecnico(self):
        return self._importe_tecnico
    
    
    # Setters
    
    @horas_parada.setter
    def horas_parada(self, horas_parada):
        self._horas_parada = horas_parada        
    
    @importe_tecnico.setter
    def importe_tecnico(self, importe_tecnico):
        self._importe_tecnico = importe_tecnico 
    
    # Metodo abstracto para calcular el gasto total
    def gasto_total(self):
        return float(self._importe_repuestos) + float(self._importe_tecnico)      
    
    
    # toString
        
    def __str__(self):            
        return super().__str__() + f", Mantenimiento Correctivo ( Horas paradas: {self._horas_parada}, Importe tecnico: {self._importe_tecnico})"
            
        
        