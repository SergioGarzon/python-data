'''
Empleado de una empresa
Crear una clase Empleado con legajo, nombre, sueldo y antigüedad en años. Implementar el constructor y __str__().
Agregar un método aumentar_sueldo(porcentaje) y otro método es_antiguo() que retorne True cuando el empleado
tenga 10 años o más de antigüedad. Crear al menos dos empleados y probar los métodos
'''

def imprimir_datos(datos_empleado, porcentaje_aumento):    
    print("Datos sin aumento de sueldo")
    print(datos_empleado)
    empleado_1.aumentar_sueldo(porcentaje_aumento)
    print("Datos con aumento de sueldo del 15%")
    print(datos_empleado)
    print("Es antiguo" if datos_empleado.es_antiguo() else "No es antiguo")


from Clases_Exercises.Exercise_clases_3.Empleado import Empleado

empleado_1 = Empleado(1234, "Maria", 12355.5, 44)
empleado_2 = Empleado(1487, "Pedro", 54545.5, 1)

print("\nImprimimos datos del primer empleado")
imprimir_datos(empleado_1, 55)

print("\nImprimimos datos del segundo empleado")
imprimir_datos(empleado_2, 10)



