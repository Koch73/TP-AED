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

    #Bandera para comprobar si el arreglo esta ordenado para efectuar busqueda binaria (punto 5)
    ordenado = False
    while opc != 0:
        if opc == 1:
            decision = int(input("Estas seguro de que deseas eliminar el registro anterior y crear uno nuevo si(1) no (0): "))
            if decision == 1:
                registros = cargarVector(registros, "peajes-tp3.txt")
                print("\nRegistros cargados satisfactoriamente.\n")

        elif opc == 2:
            cargaPorTeclado(registros)
            print("\nRegistro cargado satisfactoriamente.\n")

        elif opc == 3:
            registros = ordenarRegistros(registros)
            mostrarRegistros(registros)
            print("\nRegistros ordenados de forma ascendente.\n")
            ordenado = True

        elif opc == 4:
            patente_buscada = input("\nIngrese la patente que desea buscar: ")
            cabina_buscada = input("Ingrese el país de la cabina: ")

            resultado4 = buscarRegistro(registros, patente_buscada, cabina_buscada)
            if not(resultado4):
                print("\nNo se encontró el registro deseado")
            else:
                print("\n", resultado4)

        elif opc == 5:
            if not ordenado:
                registros = ordenarRegistros(registros)

            codigo_buscado = input("Ingrese el código buscado: ")
            indice = buscarCodigo(registros, codigo_buscado)
            if indice == False:
                print("\nNo se encontro el codigo")
            else:
                registros = cambiarValor(registros, indice)
                print("\nEl registro modificado: ", registros[indice])

        elif opc == 6:
            lista_nombres_paises, lista_paises = cantidadVehiculos(registros)
            mostrarPaises(lista_nombres_paises, lista_paises)

        elif opc == 7:
            pass
        elif opc == 8:
            pass
        elif opc == 9:
            pass
        opc = int(input('\nOpcion: '))

def Main():
    registros = []
    menu(registros)

if __name__ == "__main__":
    Main()


