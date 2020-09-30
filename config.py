from fake_useragent import UserAgent
import dotenv


def create_random_agent():
    return UserAgent().random


class Config:
    BAN_SOCIEDADES = [
        'REINHOLD',
    ]

    PATRONES_RAZON_SOCIAL = [
        r'SOCIEDADES\s.*\"(.*)\"',
        r'SOCIEDADES\s\/\s.*\"(.*)\" \(CONSTITUCIÓN\)"*',
        r'"(.*) \(CONSTITUCIÓN\)\"*',
        r'SOCIEDADES\s\/\s(.*)\(CONSTITUCIÓN\)',
        r'SOCIEDADES\s\/\s.*\"(.*)\" \(CONSTITUCIN\)"*',
        r'"(.*) \(CONSTITUCIN\)\"*',
        r'SOCIEDADES\s\/\s(.*)\(CONSTITUCIN\)',
        r'SOCIEDADES\s\/\s"(.*)\"',
        r'SOCIEDADES\s\/\s(.*)\.$',
        r'SOCIEDADES\s\/\s(.*)',
        r'"(.*)"',
    ]

    PATRONES_RAZON_SOCIAL_AVISO = [
        r'\"(.*)\"',
        r'\“(.*)\”'
    ]

    URLS = {
        'base_url': 'https://boletin.tucuman.gov.ar/',
        'tabla_url': 'https://boletin.tucuman.gov.ar/tabla'

    }

    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': create_random_agent(),
        'Referer': URLS['tabla_url']
    }
    payload = {
        'tiposinstrumentos': '0',
        'TiposJudiciales': '0',
        'TiposComunes': '0',
        'fechaboletin1': None,
        'fechaboletin2': None,
        'offset': 0,
        'Submit': 'Buscar'
    }
    offset_increment = 15

    reg_ex_head_0 = r'([0-9]{5})\s{15}'
    reg_ex_head_1 = r'(\d{2}/\d{2}/\d{4})'
    reg_ex_head_2 = r'Nro:\s{15}(\d{5,6})'
    reg_ex_head_3 = r'Nro:\s{15}\d{5,6}([JUICIOS|RESOLUCIONES|DECRETO|GENERALES|VARIOS].*$)'

    reg_categorias_solicitadas = ['SOCIEDADES', 'ASAMBLEAS', 'AVISOS']

    dotenv.load('./dev.env')
    DB_AZURE = {
        'DB_HOST': dotenv.get('DB_HOST_AZURE'),
        'DB_NAME': dotenv.get('DB_NAME_AZURE', default=''),
        'DB_USER': dotenv.get('DB_USER_AZURE'),
        'DB_PASS': str(dotenv.get('DB_PASS_AZURE')),
        'DB_PORT': dotenv.get('DB_PORT_AZURE', default='3306')
    }

    DB_DOCKER = {
        'DB_HOST': dotenv.get('DB_HOST_DOCKER'),
        'DB_NAME': dotenv.get('DB_NAME_DOCKER', default=''),
        'DB_USER': dotenv.get('DB_USER_DOCKER'),
        'DB_PASS': str(dotenv.get('DB_PASS_DOCKER')),
        'DB_PORT': dotenv.get('DB_PORT_DOCKER', default='3306')
    }

    DB_PROD = {
        'DB_HOST': dotenv.get('DB_HOST_PROD'),
        'DB_NAME': dotenv.get('DB_NAME_PROD', default=''),
        'DB_USER': dotenv.get('DB_USER_PROD'),
        'DB_PASS': str(dotenv.get('DB_PASS_PROD')),
        'DB_PORT': dotenv.get('DB_PORT_DOCKER', default='3306')
    }
