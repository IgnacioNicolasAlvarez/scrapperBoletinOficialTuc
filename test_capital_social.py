import re

text = 'POR 1 DIA -Por disposicin del Sr. Director de Personas Jurdicas-Registro Pblico, el CPN Aldo Madero, ' \
       'se hace saber que por Expediente 2544/205-C-2020 de fecha 13/08/2020, se encuentra en trmite de inscripcin el ' \
       'instrumento de fecha 29 de Julio del ao 2020, mediante el cual se constituye la sociedad "QUETUPI S.A.S (' \
       'Constitucin)", de acuerdo a lo normado en Ley 27.349, conformada por los Sres.: GARCIA MONTEROS, ' \
       'RODRIGO SEBASTIAN, D.N.I. N 34.067.762, fecha de nacimiento 08/06/1989, Soltero, de profesin Lic. ' \
       'Administracin de Empresas, domiciliado en calle Santa Fe N 955, piso 5 depto. G, de la ciudad de San Miguel ' \
       'de Tucumn, Provincia de Tucumn; ROJAS, RAUL MATIAS GONZALO, D.N.I. N 37.096.373, fecha de nacimiento ' \
       '02/10/1992, Soltero, de profesin Comerciante, domiciliado en calle 25 de Mayo N 759, piso 4 depto. B, ' \
       'de la ciudad de San Miguel de Tucumn, Provincia de Tucumn.- Domicilio: La sociedad establece su domicilio ' \
       'social y legal en calle 25 de Mayo N 759, piso 4 depto. B, localidad San Miguel de Tucumn, Provincia de ' \
       'Tucumn.- Plazo de Duracin: La duracin de la sociedad ser de 99 (noventa y nueve) aos a partir de la ' \
       'inscripcin en el Registro Pblico de Tucumn.-Designacin de su Objeto: La sociedad tiene por objeto realizar, ' \
       'por cuenta propia, de terceros o asociada a terceros, en el pas o en el extranjero, las siguientes ' \
       'actividades: COMERCIAL: La compra, venta, produccin, importacin, exportacin, intermediacin de equipos, ' \
       'perifricos, accesorios e insumos de computacin y aparatos de telefona y comunicacin y sus accesorios, ' \
       'al por mayor y/o menor, todo esto por cuenta propia o ejerciendo representacin, mandatos, comisiones o ' \
       'representaciones, franquicias y/o concesiones de terceros.-Capital Social: El capital social se establece en ' \
       'la suma de $ 300.000,(Pesos Trescientos mil),dividido en 3000 (tres mil)acciones ordinarias nominativas no ' \
       'endosables de $100-(Pesos Cien) de valor nominal cada una, totalmente suscriptas por cada uno de los socios ' \
       'con el siguiente detalle: el Sr. GARCIA MONTEROS, RODRIGO SEBASTIAN, 2100 acciones, y el Sr. ROJAS, ' \
       'RAUL MATIAS GONZALO, 900 acciones.- Organizacin de la Administracin: La administracin estar a cargo de ' \
       'RODRIGO SEBASTIAN, GARCIA MONTEROS, D.N.I. N 34.067.762.La representacin legal estar a cargo deRODRIGO ' \
       'SEBASTIAN, GARCIA MONTEROS, D.N.I. N 34.067.762.- Fecha de Cierre de Ejercicio: el ejercicio social cerrar el ' \
       '30 de Abril de cada ao. SAN MIGUEL DE TUCUMAN, 28de septiembre de 2020. E y V 29/09/2020. $885,85. Aviso N ' \
       '232.780. '



def encontrarCapitalSocial(string):
    patronPrecio = re.compile(r'(\$[0-9]*)')
    patron = re.compile(r'\s+')
    palabras = [pipeline(x) for x in patron.split(string)]
    precios = []
    numMayor = 0

    for i in palabras:
        encontrado = re.search(patronPrecio, i)
        if encontrado:
            precios.append((encontrado.group()[1:]))

    print(precios)
    for pre in precios:
        precioInt = 0 if pre is None or pre is '' else int(pre)
        if precioInt > numMayor:
            numMayor = precioInt

    return numMayor if numMayor > 5000 else 0


def pipeline(numero):
    return eliminar_espacio_signo_peso(eliminar_decimales(eliminar_punto_mil(numero)))


def eliminar_decimales(numero):
    aux = re.search(r"\.[0-9]{2}(?![0-9]+)", numero)
    if aux:
        numero = ''.join(list(numero)[:aux.start()])
    return numero.replace('.', '')


def eliminar_punto_mil(numero):
    aux = re.search(r"\$\s*[0-9]{2,3}(\.)[0-9]{2,3}", numero)
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


print(encontrarCapitalSocial(text))
