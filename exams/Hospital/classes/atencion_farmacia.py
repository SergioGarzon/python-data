# Una atención de farmacia agregan los siguientes datos: el importe total de los medicamentos
# vendidos en dicha atención; y un cupón de descuento que especifica el monto de descuento 
# que se aplicaría sobre el importe total de los medicamentos; en caso que el cupón de 
# descuento sea igual que 0, no se realizará ningún descuento; cabe aclarar que el cupón 
# de descuento debe ser 0 o positivo.

from classes.atencion import Atencion

class AtencionFarmacia(Atencion):
    
    _importe_total_medicamentos = None
    _cupon_descuento = None # Especifica el monto de descuento
    
    def __init__(self, codigo, tipoDeCobro, importe_total_medicamentos, cupon_descuento):
        super().__init__(codigo, tipoDeCobro)
        self._importe_total_medicamentos = importe_total_medicamentos
        self._cupon_descuento = cupon_descuento
        
    # Getter
    
    @property
    def importe_total_medicamentos(self):
        return self._importe_total_medicamentos
    
    @property
    def cupon_descuento(self):
        return self._cupon_descuento
    
    # Setter
    
    @importe_total_medicamentos.setter
    def importe_total_medicamentos(self, importe_total_medicamentos):
        self._importe_total_medicamentos = importe_total_medicamentos
        
    @cupon_descuento.setter
    def cupon_descuento(self, cupon_descuento):
        self._cupon_descuento = cupon_descuento
        
    
        
    # Metodo para calcular lo que se solicita
    
    '''
    El importe total de las atenciones de farmacia se calcula a partir del importe total de 
    los medicamentos vendidos. 
    
    Luego se le realiza el descuento del cupón de descuento cuyo importe está especificado. 
    
    Por último, si el tipo de cobro es igual a 2 (“tarjeta de crédito”) 
    se leincrementa al anterior importe un 30% más; en caso que el cobro sea igual a 1 (“efectivo”) 
    se le realiza un descuento del 5% sobre elanterior importe.
    '''  
    def importeACobrar(self):
        
        recargo = 0.0
        descuento = 0.0
        
        match self._tipoDeCobro:
            case "1": descuento = descuento + (self._importe_total_medicamentos * 0.05)
            case "2": recargo = recargo + (self._importe_total_medicamentos * 0.3)             
        
        resultado = self._importe_total_medicamentos - self._cupon_descuento - descuento + recargo
        
        return float(resultado)
        
    
    
    # toString
    
    def __str__(self):
        return super().__str__() + f", Atencion farmacia (Importe total medicamentos: {self._importe_total_medicamentos}, monto cupon descuento: {self._cupon_descuento} )"
    
    
    