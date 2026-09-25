# legajo, nombre, sueldo y antigüedad en años

class Empleado:
    
    def __init__(self, legajo, nombre, sueldo, antiguedad_anios):
            self.legajo = legajo
            self.nombre = nombre
            self.sueldo = sueldo
            self.antiguedad_anios = antiguedad_anios            

    def aumentar_sueldo(self, porcentaje):
        self.sueldo += ((self.sueldo * porcentaje) / 100)
        
    def es_antiguo(self):
        return self.antiguedad_anios > 10

    def __str__(self):
        return (
            "{ Legajo: " + str(self.legajo) + 
            ", Nombre: " + str(self.nombre) + 
            ", Sueldo: " + str(self.sueldo) + 
            ", Antiguedad años: " + str(self.antiguedad_anios) +
            " }"
        )