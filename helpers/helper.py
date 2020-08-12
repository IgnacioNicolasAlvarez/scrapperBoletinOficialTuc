import requests
from bs4 import BeautifulSoup
from helpers.expresionesRegularesF import *


def get_head_attr(pattern, text):
    return re.findall(pattern, text)[0]


def _get_text_from_aviso(bs):
    main_text = bs.find_all("tr", {'bgcolor': '#E4ECED'})
    return main_text[1].find_all('p')[1].get_text()


def get_dic_from_urls(config, links):
    aviso = []

    for link in links:
        link = config.URLS['base_url'] + link
        response = requests.get(link, headers=config.headers)
        bs = BeautifulSoup(response.text, 'html.parser')
        tr = bs.find_all("tr", {'valign': 'middle'})

        #        'header': ['29774', '15/07/2020', '231412', 'SOCIEDADES / ACHERAL SA']}]

        for td in tr:
            aviso.append(create_dic(config, bs, td))

    return aviso


def create_dic(config, bs, td):
    text = _get_text_from_aviso(bs)
    return {
        'text': text,
        'nro_boletin': get_head_attr(pattern=config.reg_ex_head_0, text=td.get_text().replace('\n', '')),
        'fecha_aviso': get_head_attr(pattern=config.reg_ex_head_1, text=td.get_text().replace('\n', '')),
        'nro_aviso': get_head_attr(pattern=config.reg_ex_head_2, text=td.get_text().replace('\n', '')),
        'tipo_aviso': get_head_attr(pattern=config.reg_ex_head_3, text=td.get_text().replace('\n', '')),
        'titulo': encontrarIdTitulo(text),
        'fechaConstitucion': encontrarFechaConstitucion(text),
        'CUIT': encontrarCUIT(text),
        'capitalSocial': encontrarCapitalSocial(text) if (encontrarCapitalSocial(text) is not None) else 0.00
    }
