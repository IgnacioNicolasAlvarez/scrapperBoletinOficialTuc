import re
import datetime
from config import Config

def encontrarIdBoletin(text):
    patronIdBoletin = r'(A[0-9]{6})'
    encontrado = re.search(patronIdBoletin, text)
    if encontrado:
        return encontrado.group()
    return None


def encontrarFecha(text):
    patronfecha = r'([0][1-9]|[12][0-9]|3[01])(\/|-)([0][1-9]|[1][0-2])\2(\d{4})'
    encontrado = re.search(patronfecha, text)
    if encontrado:
        fecha = datetime.datetime.strptime(encontrado.group(), '%d/%m/%Y')
        return fecha.date()
    return None


def encontrarFechaConstitucionSAS(texto):
    patronfecha = r'([0][1-9]|[12][0-9]|3[01])(\/|-)([0][1-9]|[1][0-2])\2(\d{4})'
    patron = re.compile(r'\s+')
    palabras = patron.split(texto)
    textoAnalizar = palabras[1]

    encontrado = re.search(patronfecha, textoAnalizar)
    if encontrado:
        fecha = datetime.datetime.strptime(encontrado.group(), '%d/%m/%Y')
        return fecha.date()
    print("No se ha encontrado ninguna fecha")
    return None


def encontrarCUIT(texto):
    patronfecha = r'\b(30|33|34)(\D)?[0-9]{8}(\D)?[0-9]'
    encontrado = re.search(patronfecha, texto)
    if encontrado:
        return encontrado.group()
    return ''


def encontrarFechaConstitucion(texto):
    patronfecha = r'([0][1-9]|[12][0-9]|3[01])(\/|-)([0][1-9]|[1][0-2]|[1-9])\2(\d{4})'
    patronSeparar = re.compile(r'\s+')
    palabras = patronSeparar.split(texto)
    fechas = []
    fecha_referencia = datetime.datetime.strptime('01/01/2017', '%d/%m/%Y')

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

    for fecha in fechas:
        try:
            fecha_aux = datetime.datetime.strptime(fecha, '%d/%m/%Y')
        except:
            continue
        if fecha_aux > fecha_referencia:
            fecha_referencia = fecha_aux

    return fecha_referencia.date().strftime('%Y-%m-%d')


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
    patron1 = re.compile(r'\bS.R.L|SOCIEDAD DE RESPONSABILIDAD LIMITADA|SRL|S.R.L.|S R L$\b')
    patron2 = re.compile(r'\bS.A.$|S.A$|S A|S. A.|S. A\b')
    patron3 = re.compile(r'\bS\.C\.$|SOCIEDAD CIVIL|S\.C$|SC$|S C$|S.C.\b')
    patron5 = re.compile(r'\bASOCIACION MUTUAL|ASOCIACIÓN MUTUAL\b')
    patron9 = re.compile(r'\bS.H.$|SOCIEDAD COLECTIVA|S.H$|SH$|S H$\b')
    patron12 = re.compile(r'\bS.C.$|S.C$|SC$|S C$\b')
    patron14 = re.compile(r'\bU\.T\.E\.$|U\.T\.E$|UTE$|U T E$\b')
    patron29 = re.compile(r'\bS\.C\.S\.$|SOCIEDAD EN COMANDITA SIMPLE|S\.C\.S$|SCS$|S C S$\b')
    patron30 = re.compile(
        r'\bS.A.S.|S. A. S.|S .A .S|SOCIEDAD ANÓNIMA SIMPLIFICADA|SOCIEDAD ANONIMA SIMPLIFICADA|S\.A\.S$|SAS$|SAS.|S A S$|SAS - Sociedad Anónima Simplificada\b')
    patron38 = re.compile(r'\bS\.C\.A\.$|SOCIEDAD EN COMANDITA POR ACCIONES|S\.C\.A$|SCA$|S C A$\b')
    patron41 = re.compile(r'\bS\.C\.I\.$|SOCIEDAD DE CAPITAL E INDUSTRIA|S\.C\.I$|SCI$|S C I$\b')
    patron42 = re.compile(r'\bCOOPERATIVA\b')
    patron43 = re.compile(r'\bFIDEICOMISO\b')
    patron45 = re.compile(r'\bA\.C\.$|ASOCIACION CIVIL|ASOCIACIÓN|ASOCIACION|ASOCIACIÓN CIVIL|A\.C$|AC$|A C$\b')
    patron46 = re.compile(r'\bAGRUPACION DE COLABORACION EMPRESARIA|AGRUPACIÓN DE COLABORACIÓN EMPRESARIA\b')
    patron47 = re.compile(r'\bSOCIEDAD POR ACCIONES SIMPLIFICADA\b')

    encontrado = re.search(patron30, string)
    if encontrado:
        return "30"

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
    return "44"


def get_razon_social(text):
    text = text.replace('"', '')
    try:
        return re.findall(r"SOCIEDADES / (.*)", text)[0]
    except Exception as e:
        return None


def encontrarCapitalSocial(string):
    patronPrecio = re.compile(r'(\$[0-9]*)')
    palabras = [eliminar_decimales(x) for x in re.compile(r'\s+').split(string)]
    palabras = [eliminar_espacio_signo_peso(x) for x in palabras]
    precios = []
    numMayor = 0

    for pal in palabras:
        encontrado = re.search(patronPrecio, pal)
        if encontrado:
            precios.append((encontrado.group()[1:]))

    for pre in precios:
        precioInt = 0
        try:
            precioInt = int(pre)
        except:
            pass
        numMayor = precioInt if precioInt > numMayor else numMayor

    return numMayor if numMayor > 5000 else 0


def eliminar_decimales(numero):
    aux = re.search(r"\.[0-9]{2}(?![0-9]+)", numero)
    if aux:
        numero = ''.join(list(numero)[:aux.start()])
    return numero.replace('.', '')


def eliminar_espacio_signo_peso(texto):
    aux = re.search(r"(\$\s[0-9]*)", texto)
    if aux:
        texto_sin_espacio = list(texto[aux.start(): aux.end()])
        texto_sin_espacio[1] = ''
        return ''.join(texto_sin_espacio)
    return texto
