tipo_titulos = [
    {"1": ["CONSTITUCION"]},
    {"2": ["MODIFICACION RAZON SOCIAL", "RECONDUCCION"]},
    {"5": ["DESIGNACION", "MODIFICACION AUTORIDADES", "DIRECTORIO", "GERENCIA"]},
    {"7": ["ASAMBLEA"]},
    {"10": ["ESCISION", "FUSION"]},
    {"13": ["CESION DE CUOTAS", "ACCIONES"]},
    {"14": ["APERTURA DE SUCURSAL"]},
    {"16": ["DISOLUCION", "LIQUIDACION"]},
    {"20": ["MODIFICACION ESTATUTO", "CONTRATO SOCIAL"]},
    {"27": ["MODIFICACION CAPITAL SOCIAL"]},
    {"35": ["MODIFICACION DOMICILIO"]},
    {"41": ["TRANSFORMACION"]},
    {"58": ["ACTA COMPLEMENTARIA", "RECTIFICACION", "RATIFICACION"]},
    {"66": ["MODIFICACION PLAZO"]},
    {"83": ["BALANCE"]},
    {"86": ["MODIFICACION", "AMPLIACION", "REDUCCION OBJETO SOCIAL"]},
    {"92": ["CESION DE CARTERA DE CLIENTES", "DEUDORES"]},
    {"108": ["OTROS"]},
    {"109": ["REFORMA ARTICULOS"]},
    {"110": ["AUMENTO CAPITAL"]},
    {"111": ["REDUCCION DE CAPITAL"]},
    {"112": ["EDICTO COMPLEMENTARIO"]},
    {"113": ["MODIFICACION"]},
    {"114": ["CAMBIO DENOMINACION SOCIAL"]},
    {"115": ["DESIGNACION DE SEDE SOCIAL"]},
    {"116": ["PRORROGA VIGENCIA DE SOCIEDAD"]},
    {"117": ["LICITACION"]},
    {"118": ["SOCIEDADES"]},
]


def get_tipo_aviso(text):
    for tipo in tipo_titulos:
        for key, value in tipo.items():
            for v in value:
                if v in text:
                    return key
    return 0
