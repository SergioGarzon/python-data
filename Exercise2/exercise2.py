# Procesamiento de temperaturas en una lista
# 
# Ingresar un conjunto de temperaturas en una lista, finalizar la carga cuando
# se reciba un 50. Sólo aceptar temperaturas entre -20 y 49 grados.
# 
# Calcular y mostrar:
# • Cantidad de días con temperatura bajo cero
# • Promedio de temperaturas
# • Promedio de temperaturas de los días cálidos, es decir con temp. mayor a 20
# • Mostrar “Si” o “No” para indicar si hubo algún día con más de 40 grados.
# • La mayor temperatura de los días que no fueron cálidos
# • Cantidad de días con temperatura menor al promedio

lista_temperaturas = []
temperatura = 0

while temperatura < 50:
    print("\nSe solicita ingreso de temperatura -20° y 49°, \nsi ingresa 50° finaliza la carga de datos")
    temperatura = int(input("Ingrese la temperatura:"))
    
    if temperatura < 50 and temperatura > -20:
        lista_temperaturas.append(temperatura)
    else:
        print("\nNo se puede agregar la temperatura que ingreso " + str(temperatura) + ", debido a que no cumple el rango solicitado")
else:
    print("Como ha ingresado un valor numerico mayor o igual a 50, se ha finalizado la carga de temperaturas")
        
cant_dias_temp_bajo_cero = 0
sumatoria_temperaturas = 0
sumatoria_temperatura_dias_calidos = 0
cantidad_temperatura_dias_calidos = 0
promedio_temperatura_dias_calidos = 0
promedio_temperaturas = 0
cant_dias_menor_promedio = 0
mayor_temperatura_dias_no_calidos = 0
dia_40_grados = "NO"
        
if len(lista_temperaturas) > 0:
    
    
    if lista_temperaturas[0] < 20:
        mayor_temperatura_dias_no_calidos = lista_temperaturas[0]

    for lista in lista_temperaturas:
        
        sumatoria_temperaturas += lista
        
        if lista <= 0:
            cant_dias_temp_bajo_cero += 1
            
        if lista >= 20:
            sumatoria_temperatura_dias_calidos += lista
            cantidad_temperatura_dias_calidos += 1
        
        if lista < 20:
            if mayor_temperatura_dias_no_calidos < lista:
                mayor_temperatura_dias_no_calidos = lista    
            
        if lista >= 40: 
            dia_40_grados = "SI"
    
    if len(lista_temperaturas) != 0:
        promedio_temperaturas = sumatoria_temperaturas / len(lista_temperaturas)
    
    if cantidad_temperatura_dias_calidos != 0:
        promedio_temperatura_dias_calidos = sumatoria_temperatura_dias_calidos / cantidad_temperatura_dias_calidos
    
    for lista in lista_temperaturas:
        if lista < promedio_temperaturas:
            cant_dias_menor_promedio += 1
    
    print("\n\nMOSTRAMOS LOS DATOS CALCULADOS: \n")
    print("Cantidad de dias con temperatura bajo cero es igual a: " + str(cant_dias_temp_bajo_cero))
    print("Promedio total de las temperaturas es: " + str(promedio_temperaturas))
    print("Promedio de temperatura de los dias calidos (Mayores a 20°): " + str(promedio_temperatura_dias_calidos))
    print("¿Hubo algun dia con mas de 40 grados?: " + str(dia_40_grados))
    print("Temperatura mayor en los dias no calidos (Menores a 20°): " + str(mayor_temperatura_dias_no_calidos))
    print("Cantidad de dias con temperatura menor al promedio: " + str(cant_dias_menor_promedio))
     