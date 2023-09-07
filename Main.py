from Funciones import *

def menu(registros):
    print("-"*40)
    print("Seleccione una opción" )

    print("1) Crear arreglo de registros con tickets guardados en un archivo " )
    print("2) Crear arreglo de registros con datos ingresados por teclado " )
    print("3) Mostrar todos los tickets ordenados " )
    print("4) Buscar un ticket por patente y cabina " )
    print("5) Mostrar cantidad de vehículos por cabina" )
    print("6) Mostrar importe acumulado por cada vehículo " )
    print("7) Mostrar tipo de vehículo con mayor monto acumulado y el porcentaje que representa del total " )
    print("8) Mostrar la distancia promedio recorrida y cuantos vehículos superan el promedio " )
    print("9) Calcular y mostrar la distancia promedio entre todos los"
          " vehiculos y cuales de ellos superaron ese promedio" )
    print("0) Salir " )
    print("-"*40)
    opc = int(input('Opcion: '))
    while opc != 0:
        if opc == 1:
            decision = int(input("Estas seguro de que deseas eliminar el registro anterior y crear uno nuevo si(1) no (0): "))
            if decision == 1:
                registros = cargar_vector(registros, "peajes-tp3.txt")
                print("\nRegistros cargados satisfactoriamente.\n")

        if opc == 2:
            cargaPorTeclado(registros)
            print("\nRegistro cargado satisfactoriamente.\n")

        if opc == 3:
            registros = ordenarRegistros(registros)
            print("\nRegistros ordenados de forma ascendente.\n")
            mostrarRegistros(registros)
        if opc == 4:
            pass
        if opc == 5:
            pass
        if opc == 6:
            pass
        if opc == 7:
            pass
        if opc == 8:
            pass
        if opc == 9:
            pass
        opc = int(input('\nOpcion: '))

def Main():
    registros = []
    menu(registros)

if __name__ == "__main__":
    Main()

#TERMINAR FUNCION paisPatente() PARA QUE AYUDE A MOSTRAR EL PAIS EN EL PUNTO 3
#PUNTO 4,5,6,7,8,9