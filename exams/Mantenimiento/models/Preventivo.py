# Existen dos tipos de mantenimiento, por un lado se realizan mantenimientos periódicos 
# preventivos para reemplazar insumos (tales como lubricantes o repuestos de vida útil 
# restringida) y para verificar su correcto funcionamiento. 
# 
# De estos mantenimientos preventivos 
# se registra el importe gastado en insumos y el resultado del mismo, que puede ser 1 si la 
# máquina se encuentra funcionando correctamente, 2 si se recomienda una revisión del servicio 
# técnico del fabricante y 3 si se detecta alguna rotura.  

from models.Mantenimiento import Mantenimiento

class Preventivo(Mantenimiento):
    
    _importe_insumos = None
    _resultado = None
    
    # Constructor
    
    def __init__(self, operario, fecha, importe_repuestos, importe_insumos, resultado):
        super().__init__(operario, fecha, importe_repuestos)
        self._importe_insumos = importe_insumos
        self._resultado = resultado
    
    # Getters
    
    @property
    def importe_insumos(self):
        return self._importe_insumos

    @property
    def resultado(self):
        return self._resultado
    
    # Setters
    
    @importe_insumos.setter
    def importe_insumos(self, importe_insumos):
        self._importe_insumos = importe_insumos
    
    @resultado.setter
    def resultado(self, resultado):
        self._resultado = resultado
        
    # Metodo abstracto para calcular el gasto total
    def gasto_total(self):
        return float(self._importe_repuestos) + float(self._importe_insumos)      
        
        
    # toString
    
    def __str__(self):
        
        resultado_str = ""
        
        match int(self._resultado):
            case 1: resultado_str = "Maquina funcionando correctamente"
            case 2: resultado_str = "Maquina solicita revision servicio tecnico"
            case 3: resultado_str = "Maquina con rotura"
        
        return super().__str__() + f", Mantenimiento Preventivo ( Importe insumos: {self._importe_insumos}, resultado: {resultado_str})"
        
    
    