class Persona:
    
    _dni = None
    _nombre = None
    _apellido = None
    
    def __init__(self, dni_dato, nombre_dato, apellido_dato):
        self._dni = dni_dato
        self._nombre = nombre_dato
        self._apellido = apellido_dato
        
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
    
    @nombre.setter
    def nombre(self, nombre_nuevo):
        self._nombre = nombre_nuevo
        
    @apellido.setter
    def apellido(self, apellido_nuevo):
        self._apellido = apellido_nuevo
        
    def __str__(self):
        return f"Dni: {self._dni}, \nnombre: {self._nombre}, \napellido: {self._apellido}"