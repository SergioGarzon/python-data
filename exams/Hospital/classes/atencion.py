# Cada atención tiene los siguientes datos: un código numérico que 
# identifica a cada atención; y un valor numérico que representa el tipode cobro 
# (1: “efectivo”; 2: “tarjeta de crédito”). Las atenciones pueden ser médicas o de farmacia:

from abc import ABC, abstractmethod

class Atencion(ABC):
    
    _codigo = None
    _tipoDeCobro = None
    
    def __init__(self, codigo, tipoDeCobro):
        self._codigo = codigo
        self._tipoDeCobro = tipoDeCobro        
        
    # Getters
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def tipoDeCobro(self):        
        return self._tipoDeCobro
    
    # Setters
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
    
    @tipoDeCobro.setter
    def tipoDeCobro(self, tipoDeCobro):       
        self._tipoDeCobro = tipoDeCobro
            
    # Metodo para calcular lo que se solicita
    
    @abstractmethod
    def importeACobrar(self):
        pass
    
    # toString 
    
    def __str__(self):
        
        tipo_cobro_str = ""
        
        match int(self._tipoDeCobro):
            case 1: tipo_cobro_str = "Efectivo"                
            case 2: tipo_cobro_str = "Tarjeta de crédito"
                    
        return f"Atención ( {self._codigo}, {tipo_cobro_str.upper()})"
    
