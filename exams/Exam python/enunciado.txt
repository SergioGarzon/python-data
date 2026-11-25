# EJERCICIO 8 - EQUIPAJES

Una aerolínea registra todos los equipajes transportados.  
De cada equipaje se conoce:

- `codigo` de identificación del equipaje
- `propietario` del equipaje
- `destino` al cual debe llegar el equipaje
- `peso` del equipaje
- `tarifa base` del equipaje

Existen dos tipos de equipaje:

- **Equipaje Común**: importe final igual a la tarifa base
- **Equipaje Especial**: mismo importe que el equipaje común con un recargo de $1.500 por kg transportado

El programa deberá leer los datos desde equipajes.csv y crear los objetos correspondientes.

Se deberá desarrollar lo necesario para:

1. Informar importe de cada equipaje según su tipo (aplicando polimorfismo)
2. Informar la recaudación total
3. Informar la cantidad de equipajes transportados por destino
4. Informar el destino con mayor cantidad de equipajes transportados

> Formato CSV: tipo,codigo,propietario,destino,peso,tarifa_base

> La columna `tipo` del archivo CSV **solo** determina qué objeto crear.

```
Tipo 1 = comun
Tipo 2 = especial
```
