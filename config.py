from fake_useragent import UserAgent
import dotenv


def obtener_avisos_excluidos(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        texto = archivo.readlines()
    return list(map(lambda linea: linea.replace("\n", ""), texto))


def crear_random_agent():
    return UserAgent().random


def reiniciar_config():
    dotenv.load("./.env")
    Config.OFFSET_INCREMENTO = dotenv.get("OFFSET_INCREMENTO")
    Config.PAYLOAD = {
        "tiposinstrumentos": dotenv.get("TIPOS_INSTRUMENTOS"),
        "TiposJudiciales": dotenv.get("TIPOS_JUDICIALES"),
        "TiposComunes": dotenv.get("TIPOS_COMUNES"),
        "fechaboletin1": dotenv.get("FECHA_1"),
        "fechaboletin2": dotenv.get("FECHA_2"),
        "offset": dotenv.get("OFFSET"),
        "Submit": dotenv.get("SUBMIT"),
    }


class Config:
    dotenv.load("./.env")

    AZURE_TA_KEY = dotenv.get("AZURE_TA_KEY")
    AZURE_TA_ENDPOINT = dotenv.get("AZURE_TA_ENDPOINT")

    NOMBRES_ENCARGADOS_ORG = ["Aldo Madero"]

    HORA_EJECUCION = dotenv.get("HORA_EJECUCION")

    BAN_SOCIEDADES = obtener_avisos_excluidos("AVISOS_EXCLUIDOS.TXT")

    AZURE_LIMITE_CARACTERES = dotenv.get("AZURE_LIMITE_CARACTERES")

    PATRONES_RAZON_SOCIAL = [
        r"SOCIEDADES\s.*\"(.*)\"",
        r'SOCIEDADES\s\/\s.*\"(.*)\" \(CONSTITUCIÓN\)"*',
        r'"(.*) \(CONSTITUCIÓN\)\"*',
        r"SOCIEDADES\s\/\s(.*)\(CONSTITUCIÓN\)",
        r'SOCIEDADES\s\/\s.*\"(.*)\" \(CONSTITUCIN\)"*',
        r'"(.*) \(CONSTITUCIN\)\"*',
        r"SOCIEDADES\s\/\s(.*)\(CONSTITUCIN\)",
        r'SOCIEDADES\s\/\s"(.*)\"',
        r"SOCIEDADES\s\/\s(.*)\.$",
        r"SOCIEDADES\s\/\s(.*)",
        r'"(.*)"',
    ]

    PATRONES_RAZON_SOCIAL_AVISO = [
        r"\"(.*)\"",
        r"\“(.*)\”",
    ]

    URLS = {
        "base_url": "https://boletin.tucuman.gov.ar/",
        "tabla_url": "https://boletin.tucuman.gov.ar/tabla",
    }

    HEADERS = {
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": crear_random_agent(),
        "Referer": URLS["tabla_url"],
    }

    CATEGORIAS_SOLICITADAS = ["SOCIEDADES", "ASAMBLEAS", "AVISOS"]

    REGEX_HEADER_0 = dotenv.get("REGEX_HEAD_0")
    REGEX_HEADER_1 = dotenv.get("REGEX_HEAD_1")
    REGEX_HEADER_2 = dotenv.get("REGEX_HEAD_2")
    REGEX_HEADER_3 = dotenv.get("REGEX_HEAD_3")

    OFFSET_INCREMENTO = dotenv.get("OFFSET_INCREMENTO")

    PAYLOAD = {
        "tiposinstrumentos": dotenv.get("TIPOS_INSTRUMENTOS"),
        "TiposJudiciales": dotenv.get("TIPOS_JUDICIALES"),
        "TiposComunes": dotenv.get("TIPOS_COMUNES"),
        "fechaboletin1": dotenv.get("FECHA_1"),
        "fechaboletin2": dotenv.get("FECHA_2"),
        "offset": dotenv.get("OFFSET"),
        "Submit": dotenv.get("SUBMIT"),
    }

    DB_DOCKER = {
        "DB_HOST": dotenv.get("DB_HOST_DOCKER"),
        "DB_NAME": dotenv.get("DB_NAME_DOCKER", default=""),
        "DB_USER": dotenv.get("DB_USER_DOCKER"),
        "DB_PASS": str(dotenv.get("DB_PASS_DOCKER")),
        "DB_PORT": dotenv.get("DB_PORT_DOCKER", default="3306"),
    }

    DB_PROD = {
        "DB_HOST": dotenv.get("DB_HOST_PROD"),
        "DB_NAME": dotenv.get("DB_NAME_PROD", default=""),
        "DB_USER": dotenv.get("DB_USER_PROD"),
        "DB_PASS": str(dotenv.get("DB_PASS_PROD")),
    }

    DB_MONGO = dotenv.get("DB_MONGO")

    MAIL = {
        "MAIL_DESTINO": dotenv.get("MAIL_DESTINO"),
        "MAIL_USUARIO": dotenv.get("MAIL_USUARIO"),
        "MAIL_ASUNTO": dotenv.get("MAIL_ASUNTO"),
        "MAIL_PASS": dotenv.get("MAIL_PASS"),
    }
