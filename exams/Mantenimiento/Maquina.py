from models.Correctivo import Correctivo
from models.Preventivo import Preventivo

class Maquina:
    
    _lista_mantenimientos = None
        
    def __init__(self):
        self._lista_mantenimientos = []
           
    def add_mantenimiento(self, mantenimiento):
        self._lista_mantenimientos.append(mantenimiento)
        
    def cargar_maquina(self, archivo_url):
        
        archivo_lineas = open(archivo_url)
        
        for lineas in archivo_lineas.readlines():
            linea_tupla = tuple(lineas[:-1].split(","))
            
            operario_aux = linea_tupla[2]
            fecha_aux = linea_tupla[1]
            importe_repuestos_aux = float(linea_tupla[3])
                        
            if int(linea_tupla[0]) == 1:      
                resultado_aux = int(linea_tupla[4])
                importe_insumos_aux = float(linea_tupla[5]) 
                
                # operario, fecha, importe_repuestos, importe_insumos, resultado
                mantenimiento_preventivo = Preventivo(operario_aux, fecha_aux, importe_repuestos_aux, importe_insumos_aux, resultado_aux)
                self.add_mantenimiento(mantenimiento_preventivo)
                
            if int(linea_tupla[0]) == 2: 
                horas_paradas_aux = int(linea_tupla[4])
                importe_tecnico_aux = float(linea_tupla[5])
                                
                # operario, fecha, importe_repuestos, horas_parada, importe_tecnico
                mantenimiento_correctivo = Correctivo(operario_aux, fecha_aux, importe_repuestos_aux, horas_paradas_aux, importe_tecnico_aux)
                self.add_mantenimiento(mantenimiento_correctivo)                           
                        
        archivo_lineas.close()
    
    # Mostramos datos de la lista
        
    def mostrar_datos(self):
        
        for lista in self._lista_mantenimientos:
            print(lista)
            
    # Suma de gastos
    
    def suma_gastos(self):
        
        suma_total_gastos_aux = 0.0
        
        for lista in self._lista_mantenimientos:
            
            if isinstance(lista, Correctivo):
                suma_total_gastos_aux = suma_total_gastos_aux + lista.gasto_total()
                
            if isinstance(lista, Preventivo):
                suma_total_gastos_aux = suma_total_gastos_aux + lista.gasto_total()
                
        return float(suma_total_gastos_aux)

    # Cantidad de mantenimientos caros

    def cantidad_mantenimientos_caros(self):
        
        cantidad = 0
        
        for lista in self._lista_mantenimientos:
                    
            if isinstance(lista, Correctivo):
                if (lista.gasto_total()) > 10000:
                    cantidad = cantidad + 1
                        
            if isinstance(lista, Preventivo):
                if (lista.gasto_total()) > 10000:
                    cantidad = cantidad + 1
        
        return cantidad
    
    # Rotura más larga: que informe la fecha y el nombre del operario del mantenimiento correctivo de mayor duración.
    
    def rotura_mas_larga(self):
        
        lista_ordenada = []
        
        for lista in self._lista_mantenimientos:
                            
            if isinstance(lista, Correctivo):                                               
                lista_ordenada.append(lista)
        
        lista_ordenada.sort(key=lambda p: p.horas_parada, reverse=True)
        
        primer_elemento = lista_ordenada[0]._horas_parada
        
        cadena = ""

        for lista2 in lista_ordenada:
            if primer_elemento == lista2._horas_parada:
                cadena = cadena + "{" +(lista2.operario) + ", " + str(lista2.fecha) + "}, "
        
        return cadena
    
        
    
        
    
        