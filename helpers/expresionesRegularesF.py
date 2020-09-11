import re
import datetime

patronfecha = r'([0][1-9]|[12][0-9]|3[01])(\/|-)([0][1-9]|[1][0-2]|[1-9])\2(\d{4})'
patronCUIT = r'\b(30|33|34)(\D)?[0-9]{8}(\D)?[0-9]'  # empresas


def encontrarIdBoletin(string):
    patronIdBoletin = r'(A[0-9]{6})'
    encontrado = re.search(patronIdBoletin, string)
    if encontrado:
        return encontrado.group()
    else:
        print("No se ha encontrado IdBoletin")
        return None


def encontrarFecha(string):
    patronfecha = r'([0][1-9]|[12][0-9]|3[01])(\/|-)([0][1-9]|[1][0-2])\2(\d{4})'
    encontrado = re.search(patronfecha, string)
    if encontrado:
        fechaDate = datetime.datetime.strptime(encontrado.group(), '%d/%m/%Y')
        return fechaDate.date()
    else:
        print("No se ha encontrado ninguna fecha")
        return None


def encontrarFechaConstitucionSAS(string):
    patronfecha = r'([0][1-9]|[12][0-9]|3[01])(\/|-)([0][1-9]|[1][0-2])\2(\d{4})'
    patron = re.compile(r'\s+')  # patron para dividir donde encuentre un espacio en blanco
    palabras = patron.split(string)
    textoAnalizar = palabras[1]

    encontrado = re.search(patronfecha, textoAnalizar)
    if encontrado:
        fechaDate = datetime.datetime.strptime(encontrado.group(), '%d/%m/%Y')
        return fechaDate.date()
    else:
        print("No se ha encontrado ninguna fecha")
        return None


def encontrarCapitalSocial2(string):
    patronPrecio = re.compile(r'[0-9]+((\,[0-9]+)+)?(\.[0-9]+)?(\.[0-9]+)?(\,[0-9]+)?')
    patron = re.compile(r'\s+')  # patron para dividir donde encuentre un espacio en blanco
    palabras = patron.split(string)
    precios = []
    preciosReal = []
    numMayor = 0
    preciosInt = []
    for palabra in palabras:
        bandera = 0
        encontrado = re.search(patronPrecio, palabra)
        if encontrado:
            for char in '.':
                palabra = palabra.replace(char, '')  # reemplazo los puntos

            for char in palabra:
                if char == '/' or char == '-' or char == ';' or char == ',' or char == 'º' or char == '°' or char == '%' or char == "do" or char == "2do" \
                        or char == '“' or char == '”' or char == ')' or char == 'a' or char == '(' or char == 'e' \
                        or char == ":" or char == 'ª' or char == "ro" or char == "do" or char == "to":
                    bandera = 1

        if bandera == 0:
            precios.append(palabra)

    for p in precios:
        encont = re.search(patronPrecio, p)
        if encont:
            preciosReal.append(p)

    for pre in preciosReal:
        try:
            preciosInt.append(int(pre))  # block raising an exception
        except:
            pass  # doing nothing on exception

    for pre in preciosInt:
        if pre > numMayor:
            numMayor = pre

    if preciosReal == None:
        return None

    if numMayor > 12000:
        return numMayor
    else:
        return None


def encontrarCUIT(string):
    patronfecha = r'\b(30|33|34)(\D)?[0-9]{8}(\D)?[0-9]'
    encontrado = re.search(patronfecha, string)
    if encontrado:
        return encontrado.group()
    else:
        return ""


def encontrarFechaConstitucion(string):
    patronfecha = r'([0][1-9]|[12][0-9]|3[01])(\/|-)([0][1-9]|[1][0-2]|[1-9])\2(\d{4})'  # el mes puede tener un solo número
    patronSeparar = re.compile(r'\s+')
    palabras = patronSeparar.split(string)
    fechas = []
    fechasDate = []
    fechaMayor = '01/01/2017'
    fechaMayorDate = datetime.datetime.strptime(fechaMayor, '%d/%m/%Y')

    for palabra in palabras:
        encontrado = re.search(patronfecha, palabra)
        if encontrado:
            for char in '.':
                palabra = palabra.replace(char, '')
            for char in ',':
                palabra = palabra.replace(char, '')
            for char in ';':
                palabra = palabra.replace(char, '')
            for char in '-':
                palabra = palabra.replace(char, '')
            fechas.append(palabra)

    for fecha in fechas:  # transforma las fechas en date, compara y setea la mayor
        try:
            fecha1 = datetime.datetime.strptime(fecha, '%d/%m/%Y')
            if fecha1 > fechaMayorDate:
                # return fecha1.strftime("%d/%m/%Y")
                return fecha1.date().strftime('%Y-%m-%d')
        except:
            pass


def encontrarIdTitulo(string):
    string = string.lower()
    patron5 = re.compile(
        r'\brenuncia|renunció|designa|designó|directorio|director|suplente|directora|cargo|cargos|renuncia|gerente|directores|suplentes\b')  # Designación, modificación autoridades, directorio, gerencia
    patron35 = re.compile(r'\bsede social|domicilio\b')  # modificación domicilio
    patron27 = re.compile(r'\bcapital social\b')  # modificación capital social
    patron58 = re.compile(
        r'\brectifica|ratifica|complementa|aclara\b')  # acta complementaria, rectificación, ratificación
    patron83 = re.compile(r'\bbalance|estados contables\b')  # balance
    patron10 = re.compile(r'\bescisi|escisión|fusi|fusión\b')  # escisión / fusión
    patron6 = re.compile(r'\basamblea\b')  # asamblea
    modificacion = "113"
    # si no encaja con ninguna, modificación -> 113

    encontrado = re.search(patron5, string)
    if encontrado:
        return "5"
    else:
        encontrado = re.search(patron35, string)
        if encontrado:
            return "35"
        else:
            encontrado = re.search(patron27, string)
            if encontrado:
                return "27"
            else:
                encontrado = re.search(patron58, string)
                if encontrado:
                    return "58"
                else:
                    encontrado = re.search(patron83, string)
                    if encontrado:
                        return "83"
                    else:
                        encontrado = re.search(patron10, string)
                        if encontrado:
                            return "10"
                        else:
                            encontrado = re.search(patron6, string)
                            if encontrado:
                                return "6"
                            else:
                                return modificacion


def encontrarTipoSociedad(string):
    patron1 = re.compile(r'\bS.R.L.|SOCIEDAD DE RESPONSABILIDAD LIMITADA|S.R.L\b')
    patron2 = re.compile(r'\bS.A.|SOCIEDAD ANONIMA|SOCIEDAD ANÓNIMA|S.A\b')
    patron3 = re.compile(r'\bS.C.|SOCIEDAD CIVIL|S.C\b')
    patron5 = re.compile(r'\bASOCIACION MUTUAL|ASOCIACIÓN MUTUAL\b')
    patron9 = re.compile(r'\bS.H.|SOCIEDAD COLECTIVA|S.H\b')
    patron12 = re.compile(r'\bS.C.|S.C\b')
    patron14 = re.compile(r'\bU.T.E.|U.T.E\b')
    patron29 = re.compile(r'\bS.C.S.|SOCIEDAD EN COMANDITA SIMPLE|S.C.S\b')
    patron30 = re.compile(r'\bS.A.S.|SOCIEDAD ANÓNIMA SIMPLIFICADA|SOCIEDAD ANONIMA SIMPLIFICADA|S.A.S\b')
    patron38 = re.compile(r'\bS.C.A.|SOCIEDAD EN COMANDITA POR ACCIONES|S.C.A\b')
    patron41 = re.compile(r'\bS.C.I.|SOCIEDAD DE CAPITAL E INDUSTRIA|S.C.I\b')
    patron42 = re.compile(r'\bCOOPERATIVA\b')
    patron43 = re.compile(r'\bFIDEICOMISO\b')
    # patron44 = re.compile(r'\bOTRO\b')
    patron45 = re.compile(r'\bA.C.|ASOCIACION CIVIL|ASOCIACIÓN CIVIL|A.C\b')
    patron46 = re.compile(r'\bAGRUPACION DE COLABORACION EMPRESARIA|AGRUPACIÓN DE COLABORACIÓN EMPRESARIA\b')
    patron47 = re.compile(r'\bSOCIEDAD POR ACCIONES SIMPLIFICADA\b')

    encontrado = re.search(patron1, string)
    if encontrado:
        return "1"

    encontrado = re.search(patron2, string)
    if encontrado:
        return "2"

    encontrado = re.search(patron3, string)
    if encontrado:
        return "3"

    encontrado = re.search(patron5, string)
    if encontrado:
        return "5"

    encontrado = re.search(patron9, string)
    if encontrado:
        return "9"

    encontrado = re.search(patron12, string)
    if encontrado:
        return "12"

    encontrado = re.search(patron14, string)
    if encontrado:
        return "14"

    encontrado = re.search(patron29, string)
    if encontrado:
        return "29"

    encontrado = re.search(patron30, string)
    if encontrado:
        return "30"

    encontrado = re.search(patron38, string)
    if encontrado:
        return "38"

    encontrado = re.search(patron41, string)
    if encontrado:
        return "41"

    encontrado = re.search(patron42, string)
    if encontrado:
        return "42"

    encontrado = re.search(patron43, string)
    if encontrado:
        return "43"

    encontrado = re.search(patron45, string)
    if encontrado:
        return "45"

    encontrado = re.search(patron46, string)
    if encontrado:
        return "46"

    encontrado = re.search(patron47, string)
    if encontrado:
        return "47"
    else:
        return "44"  # OTRO


def get_razon_social(text):
    try:
        return re.findall(r"SOCIEDADES / (.*)", text)[0]
    except Exception as e:
        return None


def encontrarCapitalSocialAnterior(string):  # anterior
    patronPrecio = re.compile(r'[0-9]+((\,[0-9]+)+)?(\.[0-9]+)?(\.[0-9]+)?(\,[0-9]+)?')
    patron = re.compile(r'\s+')  # patron para dividir donde encuentre un espacio en blanco
    palabras = patron.split(string)
    precios = []
    numMayor = 0
    preciosInt = []
    nuevos = []
    for palabra in palabras:
        bandera = 0
        encontrado = re.search(patronPrecio, palabra)
        if encontrado:
            for char in palabra:
                if char == '/' or char == '-' or char == ';' or char == ',' or char == 'º' or char == '°' or char == '%' or char == "do" or char == "2do" \
                        or char == '“' or char == '”' or char == ')' or char == 'a' or char == '(' or char == 'e' \
                        or char == ":" or char == 'ª' or char == "ro" or char == "do" or char == "to":
                    bandera = 1

            if bandera == 0:
                precios.append(encontrado.group())

    for pre in precios:
        nueva = pre.replace('.', '')
        nuevos.append(nueva)

    for pre in nuevos:
        try:
            preciosInt.append(int(pre))  # block raising an exception
        except:
            pass  # doing nothing on exception

    for pre in preciosInt:
        if pre > numMayor:
            numMayor = pre

    if nuevos == None:
        return 0

    if numMayor > 5000:
        return numMayor
    else:
        return 0


def encontrarCapitalSocial(string):
    patronPrecio = re.compile(r'[0-9]+((\,[0-9]+)+)?(\.[0-9]+)?(\.[0-9]+)?(\,[0-9]+)?')
    patron = re.compile(r'\s+')
    palabras = patron.split(string)
    precios = []
    numMayor = 0
    preciosInt = []
    nuevos = []
    flag = 0

    for i in range(0, len(palabras)):
        bandera = 0
        encontrado = re.search(patronPrecio, palabras[i])
        if encontrado:
            if palabras[i - 1] == "$":  # el signo peso espaciado
                for char in palabras[i]:
                    if char == '/' or char == '-' or char == ';' or char == ',' or char == 'º' or char == '°' or char == '%' or char == "do" or char == "2do" \
                            or char == '“' or char == '”' or char == ')' or char == 'a' or char == '(' or char == 'e' \
                            or char == ":" or char == 'ª' or char == "ro" or char == "do" or char == "to":
                        palabras[i] = palabras[i].replace(char, '')
                if bandera == 0:
                    precios.append(encontrado.group())

            palabra = palabras[i]
            if palabra[0] == "$":
                for char in palabra:
                    if char == '/' or char == '-' or char == ';' or char == ',' or char == 'º' or char == '°' or char == '%' or char == "do" or char == "2do" \
                            or char == '“' or char == '”' or char == ')' or char == 'a' or char == '(' or char == 'e' \
                            or char == ":" or char == 'ª' or char == "ro" or char == "do" or char == "to" or char == '$':
                        palabra = palabra.replace(char, '')
                precios.append(palabra)

    for pre in precios:
        aux = re.search(".[0-9]{2}$", pre)
        if aux:
            pre = ''.join(list(pre)[:aux.start()])
        nuevos.append(pre.replace('.', ''))

    for pre in nuevos:
        try:
            preciosInt.append(int(pre))  # block raising an exception
        except:
            pass  # doing nothing on exception

    for pre in preciosInt:
        if pre > numMayor:
            numMayor = pre

    if nuevos == None:
        return 0

    if numMayor > 5000:
        return numMayor
    else:
        return 0
