from classes.atencion_farmacia import AtencionFarmacia
from classes.atencion_medica import AtencionMedica
from classes.paciente import Paciente


class Hospital:
    
    # Del Hospital sólo interesa registrar la razón social; y una colección con todas las atenciones realizadas.
    
    _razon_social = None
    _atencion_medica_lista_principal = []    
    
    def __init__(self, razon_social):
        self._razon_social = razon_social
        self._atencion_medica_lista_principal = []
        
    def addAtencion(self, atencion):
        self._atencion_medica_lista_principal.append(atencion)
        
    def cargar_atencion_farmacia(self, archivo, archivo_2, archivo_3):
        
        lineas_archivo = open(archivo)
        
        i = 0
        
        for linea in lineas_archivo.readlines():
            
            if i != 0:
                lista = tuple(linea[:-1].split(","))
                atencion_farmacia = AtencionFarmacia(int(lista[0]), int(lista[1]), float(lista[2]), float(lista[3]))
                self._atencion_medica_lista_principal.append(atencion_farmacia)                
            
            i = i + 1
            
        lineas_archivo.close()
        
        lineas_archivo_2 = open(archivo_2)        
        
        lista_pacientes_aux = []
        i = 0
        
        for linea in lineas_archivo_2.readlines():
            if i != 0:
                lista = tuple(linea[:-1].split(","))
                lista_pacientes_aux.append(lista)                
            
            i = i + 1
                            
        lineas_archivo_2.close()
        
        lineas_archivo_3 = open(archivo_3)
        
        lista_atenciones_medicas_aux = []
        
        i = 0
        
        for linea in lineas_archivo_3.readlines():
            
            if i != 0:                
                lista = tuple(linea[:-1].split(","))
                lista_atenciones_medicas_aux.append(lista)
            
            i = i + 1
        
        i = 0
        
        paciente = None
        
        for lista in lista_atenciones_medicas_aux:
            
            for lista_2 in lista_pacientes_aux:
                
                if lista[0] == lista_2[0]:
                    if str(lista_2[3]) == 'true':
                        paciente = Paciente(str(lista_2[1]), int(lista_2[2]), True)
                    elif str(lista_2[3]) == 'false':
                        paciente = Paciente(str(lista_2[1]), int(lista_2[2]), False)
                                        
                    atencion_medica = AtencionMedica(int(lista[0]), int(lista[1]), paciente, float(lista[2]))
                    self._atencion_medica_lista_principal.append(atencion_medica)      

                
    # Mostramos los datos de la lista
    
    def mostrar_datos(self):
        
        for lista in self._atencion_medica_lista_principal:
            print(lista.__str__())
        
    # Suma de los importes de las atenciones medicas
    
    def importe_total_atencion_consulta(self):
        
        sumatoria = 0.0
        
        for lista in self._atencion_medica_lista_principal:
            sumatoria = sumatoria + lista.importeACobrar()
        
        print(sumatoria)
    
    # Promedio de los importes entre valores    
    
    def importe_promedio_atenciones(self, importe_rango_1, importe_rango_2):
        
        sumatoria = 0.0
        cantidad = 0
        
        for lista in self._atencion_medica_lista_principal:
            if lista.importeACobrar() >= importe_rango_1 and lista.importeACobrar() <= importe_rango_2:
                sumatoria = sumatoria + lista.importeACobrar()
                cantidad = cantidad + 1
            
        print(sumatoria / cantidad)
    
    
    # Retornamos el codigo de la primer atencion habitual del primer paciente
    
    def codigo_primera_atencion_habitual(self):
        
        codigo_devolver = 0
        
        self._atencion_medica_lista_principal.sort(key=lambda p: p.codigo) #, reverse=True)
        
        for lista in self._atencion_medica_lista_principal:
            if lista.paciente.habitual == True:
                codigo_devolver = (self._atencion_medica_lista_principal[0].codigo)        
                break            
                
        print(codigo_devolver)
                    
        
        

    


