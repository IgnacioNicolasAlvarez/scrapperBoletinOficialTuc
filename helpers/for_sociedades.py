tipo_sociedades = [
    {"1": "S.R.L. - SOCIEDAD DE RESPONSABILIDAD LIMITADA"},
    {"2": "S.A. - SOCIEDAD ANONIMA"},
    {"3": "SOCIEDAD CIVIL"},
    {"5": "ASOCIACION MUTUAL"},
    {"9": "S.H. - SOCIEDAD DE HECHO"},
    {"12": "S.C. - SOCIEDAD COLECTIVA"},
    {"14": "U.T.E."},
    {"29": "S.C.S. - SOCIEDAD EN COMANDITA SIMPLE"},
    {"30": "S.A.S. - SOCIEDAD ANÓNIMA SIMPLIFICADA"},
    {"38": "S.C.A. - SOCIEDAD EN COMANDITA POR ACCIONES"},
    {"41": "S.C.I. - SOCIEDAD DE CAPITAL E INDUSTRIA"},
    {"42": "COOPERATIVA"},
    {"43": "FIDEICOMISO"},
    {"44": "OTRO"},
    {"45": "A.C. - ASOCIACION CIVIL"},
    {"46": "AGRUPACION DE COLABORACION EMPRESARIA"},
    {"47": "SOCIEDAD POR ACCIONES SIMPLIFICADA"},
]


def get_tipo_sociedad(id_sociedad):
    for tipo in tipo_sociedades:
        for key, value in tipo.items():
            if key == id_sociedad:
                return value
    return None
