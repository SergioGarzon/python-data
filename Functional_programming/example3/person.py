class Persona:
    
    _dni = None
    _nombre = None
    _apellido = None
    
    def __init__(self, dni, nombre, apellido):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        
    @property
    def dni(self):
        return self._dni
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido
    
    @dni.setter
    def dni(self, dni_nuevo):
        self._dni = dni_nuevo
    
    
    