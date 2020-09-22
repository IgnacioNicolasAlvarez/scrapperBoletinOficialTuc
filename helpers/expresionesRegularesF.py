import re
import datetime
from config import Config
from helpers.for_sociedades import STRING_SOCIEDADES


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


def reemplazar_caracteres_especiales(text):
    return text.replace('.', '').replace(',', '').replace(';', '').replace('-', '')


def encontrarFechaConstitucion(texto):
    patronfecha = r'([0][1-9]|[12][0-9]|3[01])(\/|-)([0][1-9]|[1][0-2]|[1-9])\2(\d{4})'
    patronSeparar = re.compile(r'\s+')
    palabras = patronSeparar.split(texto)
    fechas = []
    fecha_referencia = datetime.datetime.strptime('01/01/2017', '%d/%m/%Y')

    for palabra in palabras:
        if re.search(patronfecha, palabra):
            palabra = reemplazar_caracteres_especiales(palabra)
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
    patron35 = re.compile(r'\bsede social|domicilio\b')
    patron27 = re.compile(r'\bcapital social\b')
    patron58 = re.compile(
        r'\brectifica|ratifica|complementa|aclara\b')
    patron83 = re.compile(r'\bbalance|estados contables\b')
    patron10 = re.compile(r'\bescisi|escisión|fusi|fusión\b')
    patron6 = re.compile(r'\basamblea\b')

    if re.search(patron5, string):
        return "5"
    elif re.search(patron35, string):
        return "35"
    elif re.search(patron27, string):
        return "27"
    elif re.search(patron58, string):
        return "58"
    elif re.search(patron83, string):
        return "83"
    elif re.search(patron10, string):
        return "10"
    elif re.search(patron6, string):
        return "6"
    return "113"


def encontrarTipoSociedad(string):
    string = string.strip()
    patron1 = re.compile(r'S.R.L|SOCIEDAD DE RESPONSABILIDAD LIMITADA|SRL|S.R.L.|S R L$')
    patron2 = re.compile(r'S.A.|S.A|S A|S. A.|S. A|SA')
    patron3 = re.compile(r'S\.C\.$|SOCIEDAD CIVIL|S\.C$|SC$|S C$|S.C.')
    patron5 = re.compile(r'ASOCIACION MUTUAL|ASOCIACIÓN MUTUAL')
    patron9 = re.compile(r'S.H.$|SOCIEDAD COLECTIVA|S.H$|SH$|S H$')
    patron12 = re.compile(r'S.C.$|S.C$|SC$|S C$')
    patron14 = re.compile(r'U\.T\.E\.$|U\.T\.E$|UTE$|U T E$')
    patron29 = re.compile(r'S\.C\.S\.$|SOCIEDAD EN COMANDITA SIMPLE|S\.C\.S$|SCS$|S C S$')
    patron30 = re.compile(
        r'S.A.S.|S. A. S.|S .A .S|SOCIEDAD ANÓNIMA SIMPLIFICADA|SOCIEDAD ANONIMA SIMPLIFICADA|S\.A\.S$|SAS$|SAS.|S A S$|SAS - Sociedad Anónima Simplificada')
    patron38 = re.compile(r'S\.C\.A\.$|SOCIEDAD EN COMANDITA POR ACCIONES|S\.C\.A$|SCA$|S C A$')
    patron41 = re.compile(r'S\.C\.I\.$|SOCIEDAD DE CAPITAL E INDUSTRIA|S\.C\.I$|SCI$|S C I$')
    patron42 = re.compile(r'COOPERATIVA')
    patron43 = re.compile(r'FIDEICOMISO')
    patron45 = re.compile(r'A\.C\.$|ASOCIACION CIVIL|ASOCIACIÓN|ASOCIACION|ASOCIACIÓN CIVIL|A\.C$|AC$|A C$')
    patron46 = re.compile(r'AGRUPACION DE COLABORACION EMPRESARIA|AGRUPACIÓN DE COLABORACIÓN EMPRESARIA')
    patron47 = re.compile(r'SOCIEDAD POR ACCIONES SIMPLIFICADA')

    if re.search(patron30, string):
        return "30"
    elif re.search(patron1, string):
        return "1"
    elif re.search(patron2, string):
        return "2"
    elif re.search(patron3, string):
        return "3"
    elif re.search(patron5, string):
        return "5"
    elif re.search(patron9, string):
        return "9"
    elif re.search(patron12, string):
        return "12"
    elif re.search(patron14, string):
        return "14"
    elif re.search(patron29, string):
        return "29"
    elif re.search(patron38, string):
        return "38"
    elif re.search(patron41, string):
        return "41"
    elif re.search(patron42, string):
        return "42"
    elif re.search(patron43, string):
        return "43"
    elif re.search(patron45, string):
        return "45"
    elif re.search(patron46, string):
        return "46"
    elif re.search(patron47, string):
        return "47"
    return "44"


def get_razon_social(text):
    text = text.replace('"', '')
    return re.findall(r"SOCIEDADES / (.*)", text)[0]


def es_razon_social_solicitada(text):
    list_palabras = text.split()
    for sociedad in STRING_SOCIEDADES:
        if sociedad in list_palabras:
            return True
    return False


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
