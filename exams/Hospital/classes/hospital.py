class Hospital:
    
    def __init__(self, razon_social):
        self.razon_social = razon_social
        self.atencion_medica_lista = []
        
    def addAtención(self, atencion_medica):
        self.atencion_medica_lista.append(atencion_medica)
    
    def importe_total_atencion_consulta(self):
        pass
    
    def importe_promedio_atenciones(self):
        pass
    
    def codigo_primera_atencion_habitual(self):
        pass    