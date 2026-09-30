class Empleado(Persona):
    
    _legajo = None
        
    def __init__(self, nro_cliente, nombre, apellido, legajo):
        super().__init__(nro_cliente, nombre, apellido)
        self._legajo = legajo
    
    @property
    def legajo(self):
        return self._legajo

    @legajo.setter
    def legajo(self, legajo_nuevo):
        self._legajo = legajo_nuevo
    
    def __str__(self):
        return f"{super().__str__()}, legajo: {self._legajo}"
    