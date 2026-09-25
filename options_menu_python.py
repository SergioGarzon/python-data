opcion = 0

while(opcion != 6):

      print('''MENU DE OPCIONES \n
      1) Sumar numeros
      2) Restar numeros
      3) Multiplicar numeros 
      4) Dividir numeros \n
      5) Calcular el modulo de un numero \n
      6) Salir del sistema
      Ingrese opcion:
      ''')
      opcion = int(input())
      
      match(opcion):
            case 1: print("hola")
            case 6: print("Muchos exitos!")


print("El programa termino!")

