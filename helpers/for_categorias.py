from config import Config

tipo_categoria = [
    {"2": ["SOCIEDADES"]},
    {"5": ["AVISOS COMERCIALES"]},
    {"7": ["ASAMBLEAS"]},
]


def get_tipo_categoria(text):
    for tipo in tipo_categoria:
        for key, value in tipo.items():
            for v in value:
                if v in text:
                    return key
    return 0


def isCategoriaRequerida(text):
    for cat in Config.CATEGORIAS_SOLICITADAS:
        if cat in text:
            return True
    return False
