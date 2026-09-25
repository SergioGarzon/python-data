class Inmueble:
    
    def __init__(self, codigo_numerico, nombre_propietario, superficie_construccion, importe_base):
        self.codigo_numerico = codigo_numerico
        self.nombre_propietario = nombre_propietario
        self.superficie_construccion = superficie_construccion
        self.importe_base = importe_base
        
    # Setters
    
    def codigo_numerico(self, codigo_numerico):
        self.codigo_numerico = codigo_numerico    
    
    # Getters
    
    @property
    def codigo_numerico(self):
        return self.codigo_numerico    
    
    
        
    def alquileres(self):
        pass
    
        
    def __str__(self):
        return ("\n{ Código numerico: " + str(self.codigo_numerico) + 
                ", nombre propietario: " + self.nombre_propietario + 
                ", superficie de construccion: " + self.superficie_construccion + 
                ", importe base: " + self.importe_base + "}")
        