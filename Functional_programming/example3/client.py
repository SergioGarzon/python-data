class Cliente(Persona):
    
    _nro_cliente = None    
        
    def __init__(self, dni, nombre, apellido, nro_cliente):
        super().__init__(dni, nombre, apellido)
        self._nro_cliente = nro_cliente
        
    @property
    def nro_cliente(self):
        return self._nro_cliente

    @nro_cliente.setter
    def nro_cliente(self, new_nro_cliente):
        self._nro_cliente = new_nro_cliente
    
    def __str__(self):
        return f"{super().__str__()}, numero de cliente: {self.nro_cliente}"
    
        
    
    
    
    