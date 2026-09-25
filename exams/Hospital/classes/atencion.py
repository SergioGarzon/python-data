class Atencion:
    
    # tipo de cobro 1) Efectivo 2) Tarjeta de credito
    def __init__(self, codigo_atencion, tipo_cobro):
        self.codigo_atencion = codigo_atencion
        self.tipo_cobro = tipo_cobro
        
    def __str__(self):
        return f"Código atencion: {self.codigo_atencion}, tipo de cobro: {self.tipo_cobro}"