from models.equipaje import Equipaje
from models.equipaje_especial import EquipajeEspecial
from models.equipaje_comun import EquipajeComun

# Para los linters que marcan como clases no usadas
# __all__ = ["Equipaje", "EquipajeComun", "EquipajeEspecial"]

class Solucion:
    
    def __init__(self):
        self.equipajes = []
        
    def agregar(self, equipaje):
        self.equipajes.append(equipaje)
        
    def cargar_datos(self, nombre_archivo):
        archivo = open(nombre_archivo)
        
        i = 0
        
        for linea in archivo.readlines():
            if i != 0:
                codigo = tuple(linea[:-1].split(","))
                
                if codigo[0] == "1":
                    equipaje = EquipajeComun(codigo[1], codigo[2], codigo[3], codigo[4], codigo[5])   
                
                if codigo[0] == "2":
                    equipaje = EquipajeEspecial(codigo[1], codigo[2], codigo[3], codigo[4], codigo[5])
                    
                self.agregar(equipaje)
                
            i = i + 1
        
        archivo.close()
        
    # Metodo para mostrar datos
    def mostrar_datos(self):         
        print("\nDATOS DE TODOS LOS EQUIPAJES\n\n")  
                
        for lista in self.equipajes:
            print(lista.__str__())
            
        
    # Mostramos importe de cada equipaje segun su tipo
    
    def importes_equipajes(self):        
        print("\nIMPORTES EQUIPAJE COMUN\n")        
        for lista in self.equipajes:            
            if isinstance(lista, EquipajeComun):
                print(lista.propietario + ": " + str(lista.importe()))
                
        print("\n\nIMPORTES EQUIPAJE ESPECIAL\n")                
        for lista2 in self.equipajes:            
            if isinstance(lista2, EquipajeEspecial):
                print(lista2.propietario + ": " + str(lista2.importe()))
        
    # Mostramos la recaudacion total
    
    def recaudacion_total(self):
        
        recaudacion = 0.0
        
        for lista in self.equipajes:
            recaudacion += float(lista.importe())
        
        print("\n\nRecaudación total: " + str(recaudacion))
        
    # Equipajes por destino
    
    def equipajes_destino(self):
        
        print("\n\n")
        
        lista_aux = []
        
        for lista in self.equipajes:            
            lista_aux.append(lista.destino)
        
        set_sin_duplicados = set(lista_aux)
        
        contador = 0
        self.destino_cantidad = {}
        
        for set_lista in set_sin_duplicados:            
            for lista in self.equipajes:            
                if lista.destino == set_lista:
                    contador = contador + 1
            
            print(str(set_lista) + ": " + str(contador))
            self.destino_cantidad[str(set_lista)] = contador            
            
            contador = 0
        
    
    # Mostramos equipajes por destino a ver que onda    
    def equipaje_mayor_destino(self):                
        dict_ordenado_mayor = dict(sorted(self.destino_cantidad.items(), key=lambda item: item[1], reverse=True))
        print("\n\n\n")
        print(dict_ordenado_mayor)
        
        contador = 0
        datos = ""
        
        max_cantidad = list(dict_ordenado_mayor.values())[0]
        
        for clave, valor in dict_ordenado_mayor.items():            
            if valor == max_cantidad:
                contador = contador + 1
                datos += "\n" + (str(clave) + "," + str(valor))

        print("En total hay destinos con empate de cantidades: " + str(contador))
        print(datos)
            
    

if __name__ == "__main__":
    solucion = Solucion()
    solucion.cargar_datos("equipajes.csv")
    solucion.mostrar_datos()
    solucion.importes_equipajes()
    solucion.recaudacion_total()
    solucion.equipajes_destino()
    solucion.equipaje_mayor_destino()
    