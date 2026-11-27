# Del paciente asociado a la atención médica se registran: su nombre; 
# el síntoma que prevalece (1: “corazon”, 2: “pulmon”, 3: “otras”); y 
# un valor booleano que representa si el paciente es habitual (true) o no 
# (false) del hospital.

class Paciente:
    
    _nombre = None
    _sintoma = None
    _habitual = None
    
    def __init__(self, nombre, sintoma, habitual = False):
        self._nombre = nombre
        self._sintoma = sintoma
        self._habitual = habitual
        
    # Getters
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def sintoma(self):
        return self._sintoma
    
    @property
    def habitual(self):
        return self._habitual
        
    # Setters
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @sintoma.setter
    def sintoma(self, sintoma):
        self._sintoma = sintoma     
    
    @habitual.setter
    def habitual(self, habitual):
        self._habitual = habitual
    
    # toString
    
    def __str__(self):
        
        respuesta_habitualidad = ""
        
        if self._habitual:
            respuesta_habitualidad = "SI"
        else:
            respuesta_habitualidad = "NO"
                
        return f"Paciente ( Nombre: {self._nombre}, sintomas: {self._sintoma}, es habitual: {respuesta_habitualidad})"
