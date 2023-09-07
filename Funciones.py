class Ticket:
    def __init__(self, codigo  =0, patente = "", tipoV = 0, forma_de_pago = 0, pais = 0, km_Recorridos = 0):
        self.codigo = codigo
        self.patente = patente
        self.tipoV = tipoV
        self.forma_de_pago = forma_de_pago
        self.pais = pais
        self.km_Recorridos = km_Recorridos
    def __str__(self):
        p = "{:<22}".format("Código: " + str(self.codigo))
        p += "{:<22}".format("Patente: " + self.patente)
        p += "{:<22}".format("Tipo de Vehículo: " + str(self.tipoV))
        p += "{:<22}".format("Forma de Pago: " + str(self.forma_de_pago))
        p += "{:<22}".format("Pais de origen: " + str(self.pais))
        p += "{:<22}".format("Kilómetros recorridos: " + str(self.km_Recorridos))
        return p


#Verificar el pais de la patente
def definir_patente(patente):
    #ARGENTINA
    if (
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isdigit()
        and patente[3].isdigit()
        and patente[4].isdigit()
        and patente[5].isalpha()
        and patente[6].isalpha()
    ):
        pais_patente = "Argentina"

    #BOLIVIA
    elif (
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isdigit()
        and patente[3].isdigit()
        and patente[4].isdigit()
        and patente[5].isdigit()
        and patente[6].isdigit()
    ):
        pais_patente = "Bolivia"
    #BRASIL
    elif (
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isalpha()
        and patente[3].isdigit()
        and patente[4].isalpha()
        and patente[5].isdigit()
        and patente[6].isdigit()
    ):
        pais_patente = "Brasil"
    #CHILE

    elif (
        patente[0] == " "
        and patente[1].isalpha()
        and patente[2].isalpha()
        and patente[3].isalpha()
        and patente[4].isalpha()
        and patente[5].isdigit()
        and patente[6].isdigit()
    ):
        pais_patente = "Chile"
    #PARAGUAY
    elif (
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isalpha()
        and patente[3].isalpha()
        and patente[4].isdigit()
        and patente[5].isdigit()
        and patente[6].isdigit()
    ):
        pais_patente = "Paraguay"
    #URUGUAY
    elif (
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isalpha()
        and patente[3].isdigit()
        and patente[4].isdigit()
        and patente[5].isdigit()
        and patente[6].isdigit()
    ):
        pais_patente = "Uruguay"
    else:
        pais_patente = "Otro"
    return pais_patente

#Cargar vector por archivo de texto
def cargar_vector(Registros, txt):
    m = open(txt, "rt")
    line = m.readline()
    Registros = []
    n = 0
    #SALTEAR TIMESTAMP
    line = m.readline()
    while line != "":

        Registros.append(Ticket())
        Registros[n].codigo = line[0:10]
        Registros[n].patente = line[10:17]
        Registros[n].tipoV = line[17]
        Registros[n].forma_de_pago = line[18]
        Registros[n].pais = line[19]
        Registros[n].km_Recorridos = line[20:]
        n += 1
        line = m.readline()

    m.close()
    return Registros


#Validar que el codigo del ticket contenga solo numeros
def validateCodigo(codigo, n):
    if len(codigo) > n:
        return False
    for i in range(len(codigo)):
        if codigo[i].isalpha():
            return False
    return True


#Validar que la patente sea correcta
def validatePatente(patente):
    if len(patente) != 7:
        return False
    return True


#Validar que el pais sea correcto
def validatePais(pais):
    if not pais in '01234' or len(pais) != 1:
        return False
    return True


#Validar que el tipo de vehiculo sea correcto
def validateTipo(tipo):
    if not tipo in '012' or len(tipo) != 1:
        return False
    return True


#Validar que la forma de pago sea correcta
def validateFormadepago(pago):
    if not pago in '12' or len(pago) != 1:
        return False
    return True


#Validar que la distancia sea correcta
def validateKm(distancia):
    if not distancia.isdigit() or len(distancia) != 3:
        return False
    return True


#Cargar un registro por teclado
def cargaPorTeclado(Registros):

    codigo = input("Ingrese el código: ")
    while not(validateCodigo(codigo, 10)):
        print("Error, codigo incorrecto, ingreselo de nuevo.")
        codigo = input("Ingrese el código: ")

    patente = input("Ingrese la patente: ")
    while not(validatePatente(patente)):
        print("Error, patente incorrecta, ingresela de nuevo")
        patente = input("Ingrese la patente: ")

    tipoV = input("Ingrese el tipo de vehiculo: ")
    while not(validateTipo(tipoV)):
        print("Error, tipo de vehiculo incorrecto, ingreselo de nuevo")
        tipoV = input("Ingrese el tipo de vehiculo: ")

    forma_de_pago = input("Ingrese la forma de pago: ")
    while not(validateFormadepago(forma_de_pago)):
        print("Error, forma de pago incorrecta, ingresela de nuevo")
        forma_de_pago = input("Ingrese la forma de pago: ")

    pais = input("Ingrese el país: ")
    while not(validatePais(pais)):
        print("Error, ingrese un pais correcto (0-4): ")
        pais = input("Ingrese el país: ")

    km_recorridos = input("Ingrese lo kilómetros recorridos: ")
    while not(validateKm(km_recorridos)):
        print("Error, distancia recorrida incorrecta, ingresela de nuevo")
        km_recorridos = input("Ingrese los kilómetros recorridos: ")

    TicketGenerado = Ticket()
    TicketGenerado.codigo = codigo
    TicketGenerado.patente = patente
    TicketGenerado.tipoV = tipoV
    TicketGenerado.forma_de_pago = forma_de_pago
    TicketGenerado.pais = pais
    TicketGenerado.km_Recorridos = km_recorridos
    Registros.append(TicketGenerado)


#Agregar los 0 que sean necesarios (x) a los componentes de una lista t
def agregarCeros(Registros, x):
    for i in range(len(Registros)):
        if len(str(Registros[i].codigo)) != x:
            cant_ceros = x - (len(str(Registros[i].codigo)))
            str_ceros = "0" * cant_ceros
            Registros[i] = str_ceros + str(Registros[i].codigo)
    return Registros


#Ordenar mediante selection sort los registros de una lista v
def ordenarRegistros(Registros):
    # array auxiliar almacena solo los codigos para luego ordenarlos
    #t = []

    #for i in range(len(Registros)):
        #ticket = Registros[i]
        #codigo_ticket = int(ticket.codigo)
        #t.append(codigo_ticket)

    #ordenamiento por seleccion directa
    n = len(Registros)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if Registros[i].codigo > Registros[j].codigo:
                Registros[i], Registros[j] = Registros[j], Registros[i]

    #agregarle los 0 que falta delante de los codigos
    Registros = agregarCeros(Registros, 10)

    return Registros


#Mostrar registros de la lista ordenados
def mostrarRegistros(Registros):
    for i in range(len(Registros)):
        paisPatente = definir_patente(Registros[i].patente)
        r = f"Pais de la patente: {paisPatente}, {Registros[i]}"
        print(r)


#Buscar registro con la patente p en el pais x
def buscarRegistro(Registros, p, x):

    #Linear search
    for i in range(len(Registros)):
        if Registros[i].patente == p and Registros[i].pais == x:
            return Registros[i]

    return False


#Buscar mediante busqueda binaria el codigo c en los registros
def buscarCodigo(Registros, c):
    # Linear search
    for i in range(len(Registros)):
        if Registros[i].codigo == c:
            return i

    return False


#Cambia el valor de la forma de pago de 1 a 2 y viceversa
def cambiarValor(Registros,indice):
    if Registros[indice].forma_de_pago == "1":
        Registros[indice].forma_de_pago = "2"
    else:
        Registros[indice].forma_de_pago = "1"

    return Registros