import re

text = 'POR UN DÍA - Se hace saber que por Expediente N° 2481/205-S-2020 de fecha 11/08/2020, se encuentra en trámite la inscripción del instrumento de fecha 19/09/2019 mediante el cual se inscriben dos cesiones de cuotas, la primera de fecha 11/08/2016, mediante la cual el Sr. Acosta Luis Alberto Antonio, DNI 08.285.272, casado, con domicilio en Buenos Aires N° 288 de la ciudad de San Miguel de Tucumán, de profesión abogado, vende, cede y transfiere 100 cuotas que le pertenecen de la sociedad "SOCIAL MED S.R.L." de la siguiente manera; vende, cede y transfiere 50 cuotas a la Sra. Romero María Soledad, DNI 28.824.730, soltera, de profesión abogada con domicilio en calle Marcos Paz N° 420, piso 5, Dpto "A" de la ciudad de San Miguel de Tucumán y vende, cede y transfiere 50 cuotas al Sr. Rojas Adrián Ernesto, soltero,  DNI 27.694.359, de profesión empresario, con domicilio en calle Monteagudo N° 476, 1° "B" de la ciudad de San  Miguel de Tucumán. Posteriormente en la segunda cesión de cuotas, la Sra. Romero María Soledad, vende, cede y transfiere, por medio de contrato de cesión de cuotas de fecha 12/02/2019, 50 cuotas sociales a la Sra.Wagner Agustina, DNI 28.886.827, argentina, casada, con domicilio en Bascary N° 850, Yerba Buena. Como consecuencia de éstos actos, se modifica el artículo cuarto del capital social, quedando redactado de la siguiente forma: El capital social se fija en la suma de PESOS  VEINTE MIL ($20.000), dividido 200 cuotas de valor nominal $100 (pesos cien) cada una , las cuales se encuentran totalmente suscriptas por los socios según el siguiente detalle:  a) La Sra. Wagner Agustina 75% (setenta y cinco por ciento del total del capital) consistente en 150 (ciento cincuenta) cuotas, de $100 (pesos cien) cada una totalizando su aporte en PESOS QUINCE MIL ($15.000); b) el Sr. Adrián Rojas  un 25% (veinticinco por ciento del total del capital) consistente en 50 (cincuenta) cuotas, de $100 (pesos cien) cada una totalizando su aporte en PESOS CINCO MIL($5.000); El capital social se integrará en dinero en efectivo, de la siguiente manera: el 25% al momento de ordenarse la inscripción de la sociedad en el Registro Público de Comercio, y el saldo en el plazo de 2 (dos) años desde esa fecha (art. 149 Ley 19.550). Asimismo se agrega artículo décimo cuarto: Poder Supletorio: Autorizase por la presente, al C.P.N. Eduardo Javier Chit, DNI  23.931.193, matrícula profesional N° 4838 C.G.C.E.T. y a la Srta. Ana Ruth Cárdenas Acuña, DNI 32.134.730, para realizar en forma conjunta, alternada o indistintamente todos los trámites legales de inscripción de las modificaciones contractuales de la sociedad ante el Registro Público, con facultad de aceptar o proponer modificaciones a este instrumento constitutivo, incluyendo el nombre social, otorgar instrumentos públicos y/o privados complementarios y proceder a la individualización de los libros sociales y contables ante el Registro Público. Asimismo, se los autoriza para realizar todos los trámites que sean necesarios ante entidades financieras, la Administración Federal de Ingresos Públicos (A.F.I.P.), Dirección General de Rentas (DGR), Dirección de Ingresos Municipales (DIM) y Administración Nacional de Aduanas y/o todo otro organismo público o privado, quedando facultados incluso para solicitar la publicación del aviso en el diario de publicaciones legales. Y en Acta complementaria del contrato social se designan como Gerentes de la firma a Wagner Agustina y Rojas Adrián Ernesto, quienes podrán actuar en forma conjunta, unilateral o alternadamente. Ambos aceptan el cargo. SAN MIGUEL DE TUCUMAN, 01 de Septiembre de 2020.- E y V 10/09/2020.- $1277,50 AVISO N° 232.422'


def encontrarCapitalSocial(string):
    patronPrecio = re.compile(r'(\$[0-9]*)')
    patron = re.compile(r'\s+')
    palabras = [eliminar_decimales(x) for x in patron.split(string)]
    palabras = [eliminar_espacio_signo_peso(x) for x in palabras]
    precios = []
    numMayor = 0

    for i in palabras:
        encontrado = re.search(patronPrecio, i)
        if encontrado:
            precios.append((encontrado.group()[1:]))

    for pre in precios:
        precioInt = int(pre)
        if precioInt > numMayor:
            numMayor = precioInt

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


print(encontrarCapitalSocial(text))
