carg = 0
cbol = 0
cbra = 0
cchi = 0
cpar = 0
curu = 0
cotr = 0
imp_acu_total = 0
idioma = ""
primera = ""
cpp = 0
mayimp = 0
maypat = ""
total_de_patentes = 0
porc = 0
cabinas_brasileras = 0
prom = 0
distancia = 0

def importe_final_acumulado(importe):
    global imp_acu_total
    imp_acu_total += int(importe)
def mostrar_resultados():
    print('(r1) - Idioma a usar en los informes:', idioma)

    print()
    print('(r2) - Cantidad de patentes de Argentina:', carg)
    print('(r2) - Cantidad de patentes de Bolivia:', cbol)
    print('(r2) - Cantidad de patentes de Brasil:', cbra)
    print('(r2) - Cantidad de patentes de Chile:', cchi)
    print('(r2) - Cantidad de patentes de Paraguay:', cpar)
    print('(r2) - Cantidad de patentes de Uruguay:', curu)
    print('(r2) - Cantidad de patentes de otro país:', cotr)

    print()
    print('(r3) - Importe acumulado total de importes finales:', imp_acu_total)

    print()
    print('(r4) - Primera patente del archivo:', primera, '- Frecuencia de aparición: ', cpp)

    print()
    print('(r5) - Mayor importe final cobrado:', mayimp, '- Patente a la que se cobró ese importe: ', maypat)

    print()
    print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')

    print()
    print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas: ', prom, '\bkm')
def importe_total(patente_u, pais):
    global maypat
    global mayimp
    global distancia
    global cabinas_brasileras
    importe_base = 0
    importe_basico = 0
    importe_final = 0
    cabinaBrasil = False

    #PAIS DE LA PATENTE
    #ARGENTINA, URUGUAY O PARAGUAY (300)
    if (patente_u[9] == "0") or (patente_u[9] == "3") or (patente_u[9] == "4"):
        importe_base = 300

    #BRASIL
    elif patente_u[9] == "2":
        importe_base = 400

        cabinaBrasil = True
        if pais == "Argentina" and cabinaBrasil:
            cabinas_brasileras = cabinas_brasileras + 1
            dt = patente_u[10] + patente_u[11] + patente_u[12]
            distancia = distancia + int(dt)


    #BOLIVIA
    elif patente_u[9] == "1":
        importe_base = 200

    #TIPO DE VEHICULO
    #MOTO
    if patente_u[7] == "0":
        importe_basico = importe_base / 2

    #AUTO
    elif patente_u[7] == "1":
        importe_basico = importe_base

    #CAMION
    elif patente_u[7] == "2":
        importe_basico = importe_base * 1.6

    #FORMA DE PAGO
    #MANUAL
    if patente_u[8] == "1":
        importe_final = importe_basico

    #TELEPEAJE
    elif patente_u[8] == "2":
        importe_final = importe_basico * 0.9

    if importe_final > mayimp:
        mayimp = int(importe_final)
        patente = ""
        for i in range(7):
            patente = patente + patente_u[i]
        maypat = patente

    importe_final_acumulado(importe_final)
def definir_patente(patente):
    pais_patente = ""
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
        global carg
        carg += 1
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
        global cbol
        cbol += 1
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
        global cbra
        cbra += 1
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
        global cchi
        cchi += 1
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
        global cpar
        cpar += 1
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
        global curu
        curu += 1
        pais_patente = "Uruguay"
    else:
        global cotr
        cotr = cotr + 1
        pais_patente = "Otro"

    importe_total(patente, pais_patente)

def analisis():

    global idioma
    global primera
    global cpp
    global total_de_patentes
    global porc
    global distancia
    global prom

    hay_e = False
    hay_p = False
    v = 0
    m = open("../Tp 2/peaje100.txt", "rt")
    line = m.readline()
    while line != "":
        v += 1
        # PRIMERA LINEA
        if v == 1:
            timestamp = line
            for i in timestamp:
                #PORTUGUES O ESPAÑOL
                if i == "P":
                    hay_p = True
                elif i == "T" and hay_p:
                    idioma = "Portugués"
                else:
                    hay_p = False
                if i == "E":
                    hay_e = True
                elif i == "S" and hay_e:
                    idioma = "Español"
                else:
                    hay_e = False
        elif v == 2:
            definir_patente(line)
            for i in range(7):
                primera = primera + line[i]
            cpp = cpp + 1
            total_de_patentes = total_de_patentes + 1

        else:
            patente = ""
            for i in range(7):
                patente = patente + line[i]
            if patente == primera:
                cpp = cpp + 1
            definir_patente(line)
            total_de_patentes = total_de_patentes + 1

        line = m.readline()

    m.close()
    if total_de_patentes > 0:
        porc = round(((cotr * 100)/total_de_patentes), 2)

    if distancia > 0:
        prom = round((distancia / cabinas_brasileras), 2)


    mostrar_resultados()



analisis()


