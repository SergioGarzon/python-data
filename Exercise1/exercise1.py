
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


surtidor = Surtidor(1, 2, 3)

print(surtidor.to_string())



