
from surtidor_class import Surtidor

# Estación de servicio
# Una estación de servicio que dispone de 10 surtidores y necesita gestionar
# información relacionada con la venta de combustibles en la jornada.
# De cada surtidor se conoce:
# • Número de Surtidor (validar que sea un número entre 1 y 30)
# • Cantidad: representa la cantidad de litros de combustible vendido por
# el surtidor (validar que sea un número positivo)
# • Tipo: representa el tipo de combustible del surtidor. Los valores que pue-
# de asumir son 1 representa “Nafta Super”, 2 representa “Nafta Especial”
# y 3 representa “Gasoil” (validar que se ingresen valores válidos).
# Se pide calcular e imprimir:
# • El total de litros vendidos en la jornada, por tipo de combustible.
# • El número de surtidor que menos combustible vendió.
# • El promedio por surtidor en litros de combustible vendido en la jornada
# (promedio general, es un único resultado)

def validate_number(mensaje):
    flag = False
    
    while flag == False:
        try:
            valor_return = int(input(str(mensaje)))
            flag = True
        except ValueError:
            print("El valor ingresado no es numerico")
            flag = False
            
    return valor_return
    

def carga_surtidores():
    surtidores_list = []    
    nro_surtidor = tipo = 0
    cantidad = -1
    
    for value_into in range(10):
        
        print("\nDatos del surtidor " + str(value_into + 1) + ": ")
        
        while nro_surtidor < 1 or nro_surtidor > 30:
            nro_surtidor = validate_number("Ingrese el numero del surtidor(Entre 1 y 30): ")
            
            if nro_surtidor < 1 or nro_surtidor > 30:
                print("Ingrese un numero de surtidor valido")  
                
        while cantidad < 0:
            cantidad = validate_number("Ingrese la cantidad del surtidor: ") 
                    
            if cantidad < 0:
                print("Ingrese una cantidad valida")       
                    
        while tipo < 1 or tipo > 3:
            tipo = validate_number("Ingrese el tipo del surtidor (1- 'Nafta Super', 2- 'Nafta Especial', 3- 'Gasoil'): ")
                    
            if tipo < 1 or tipo > 3:
                print("Ingrese un tipo de surtidor valido")
            
        surtidores_list.append(Surtidor(nro_surtidor, cantidad, tipo))
        nro_surtidor = 0
        cantidad = -1
        tipo = 0
                        
    return surtidores_list

def litros_vendidos_combustibles(datos_surtidores):
    litro_total_nafta = litro_total_nafta_especial = litro_total_gasoil = 0.0
        
    for dato in datos_surtidores:
        match dato.get_tipo():
            case 1: # Nafta Super
                litro_total_nafta += dato.get_cantidad()                
            case 2: # Nafta Especial
                litro_total_nafta_especial += dato.get_cantidad()                
            case 3: # Gasoil
                litro_total_gasoil += dato.get_cantidad() 
                            
        
    return [litro_total_nafta, litro_total_nafta_especial, litro_total_gasoil]
    

def promedio_general_cantidad(datos_surtidores):
    litro_total = 0.0
    
    for dato in datos_surtidores:
        litro_total += dato.get_cantidad()
    
    return litro_total / len(datos_surtidores)


datos_surtidores = carga_surtidores()

print("El promedio total es: " + str(promedio_general_cantidad(datos_surtidores)))

print(litros_vendidos_combustibles(datos_surtidores))




    











