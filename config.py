from fake_useragent import UserAgent
import dotenv


class Config:
    agent = UserAgent()

    URLS = {
        'base_url': 'https://boletin.tucuman.gov.ar/',
        'tabla_url': 'https://boletin.tucuman.gov.ar/tabla'
    }

    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': agent.random,
        'Referer': URLS['tabla_url']
    }
    payload = {
        'tiposinstrumentos': '0',
        'TiposJudiciales': '0',
        'TiposComunes': '0',
        'fechaboletin1': None,
        'fechaboletin2': None,
        'Submit': 'Buscar'
    }

    reg_ex_head_0 = r'([0-9]{5})\s{15}'
    reg_ex_head_1 = r'(\d{2}/\d{2}/\d{4})'
    reg_ex_head_2 = r'Nro:\s{15}(\d{5,6})'
    reg_ex_head_3 = r'Nro:\s{15}\d{5,6}([JUICIOS|RESOLUCIONES|DECRETO].*$)'

    dotenv.load('./dev.env')
    DB_AWS = {
        'DB_HOST': dotenv.get('DB_HOST_AWS'),
        'DB_NAME': dotenv.get('DB_NAME_AWS', default=''),
        'DB_USER': dotenv.get('DB_USER_AWS'),
        'DB_PASS': dotenv.get('DB_PASS_AWS')
    }
