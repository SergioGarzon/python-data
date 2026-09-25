class Hospital:
    
    def __init__(self, razon_social):
        self.razon_social = razon_social
        self.atencion_medica_lista = []
        
    def agregar_atencion(self, atencion_medica):
        self.atencion_medica_lista.append(atencion_medica)
    