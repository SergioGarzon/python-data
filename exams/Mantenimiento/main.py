
from Maquina import Maquina

if __name__ == "__main__":
    maquina = Maquina()
    maquina.cargar_maquina("./data/mantenimientos.csv")
    maquina.mostrar_datos()
    print("\n\nSuma de gastos totales: " + str(maquina.suma_gastos()))
    print("Total de mantenimiento caros: " + str(maquina.cantidad_mantenimientos_caros()))
    print("Datos maquina con rotura mas larga: " + str(maquina.rotura_mas_larga()))
    