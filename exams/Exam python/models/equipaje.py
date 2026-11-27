from abc import ABC, abstractmethod

class Equipaje(ABC):
    
    # Declaración de atributos pero no es necesaria    

    _codigo_identificacion = None
    _propietario = None
    _destino = None
    _peso = None 
    _tarifa_base = None
    
    # Constructor
    
    def __init__(self, codigo_identificacion, propietario, destino, peso, tarifa_base):
        self._codigo_identificacion = codigo_identificacion
        self._propietario = propietario
        self._destino = destino
        self._peso = peso
        self._tarifa_base = tarifa_base
    
    # Getters
    @property
    def codigo_identificacion(self):
        return self._codigo_identificacion
    
    @property
    def propietario(self):
        return self._propietario
    
    @property
    def destino(self):
        return self._destino
    
    @property
    def peso(self):
        return self._peso
    
    @property
    def tarifa_base(self):
        return self._tarifa_base
    
    # Setters
        
    @codigo_identificacion.setter
    def codigo_identificacion(self, codigo_identificacion):
        self._codigo_identificacion = codigo_identificacion
        
    @propietario.setter
    def propietario(self, propietario):
        self._propietario = propietario
    
    @destino.setter
    def destino(self, destino):
        self._destino = destino
        
    @peso.setter
    def peso(self, peso):
        self._peso = peso
    
    @tarifa_base.setter
    def tarifa_base(self, tarifa_base):
        self._tarifa_base = tarifa_base
        
    @abstractmethod
    def importe(self):
        pass
        
    # toString
    
    def __str__(self):
        return f'''Equipaje ( Código de identificación: {self._codigo_identificacion},
                Propietario: {self._propietario}, Destino: {self._destino}, Peso: {self._peso},
                Tarifa base: {self._tarifa_base} )
                '''
    
    
    