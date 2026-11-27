# Una atención médica agrega los siguientes datos: el paciente atendido; 
# y el importe de la consulta.

from classes.atencion import Atencion

class AtencionMedica(Atencion):
    
    _paciente = None
    _importe = None
    
    def __init__(self, codigo, tipoDeCobro, paciente, importe):
        super().__init__(codigo, tipoDeCobro)
        self._paciente = paciente
        self._importe = importe
    
    # Getters
    
    @property
    def paciente(self):
        return self._paciente
    
    @property
    def importe(self):
        return self._importe
    
    # Setters
    
    @paciente.setter
    def paciente(self, paciente):
        self._paciente = paciente
    
    @importe.setter
    def importe(self, importe):
        self._importe = importe
    
    # Metodo para calcular lo que se solicita
    
    '''
    El importe total de las atenciones médicas se calcula a partir del importe de la consulta. 
    
    En caso que el paciente sea “habitual” se le aplicará un descuento del 25%. 
    Por último, si el tipo de cobro es igual a 2 (“tarjeta de crédito”) se le incrementa al anterior importe un 20% más; 
    En caso que el cobro sea igual a 1 (“efectivo”) se le realiza un descuento del 10% 
    sobre el anterior importe.

    '''
    
    def importeACobrar(self):
        descuento = 0.0
        recargo = 0.0
        
        if self._paciente.habitual:
            descuento = descuento + float(self._importe) * 0.2
            
        if self._tipoDeCobro == "1": # Efectivo
            descuento = descuento + float(self._importe) * 0.1
            
        if self._tipoDeCobro == "2": # Tarjeta de Credito
            recargo = recargo + float(self._importe) * 0.2
        
        return float(self._importe - descuento + recargo)
        
        
    
    # toString
    
    def __str__(self):
        return super().__str__() + f", Atencion Medica ( Paciente: {self._paciente}, importe: {self._importe} )"
    