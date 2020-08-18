import requests
from bs4 import BeautifulSoup
from helpers.expresionesRegularesF import *
from helpers.for_titulos import get_tipo_aviso


def get_head_attr(pattern, text):
    x = []
    try:
        x = re.findall(pattern, text)[0]
    except Exception as e:
        print(e)
    print(x)
    return x


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
        text = _get_text_from_aviso(bs)
        for td in tr:
            aviso.append(create_dic(config, text, td))

    return aviso


def create_dic(config, text, td):
    return {
        'texto': text,
        'nro_boletin': get_head_attr(pattern=config.reg_ex_head_0, text=td.get_text().replace('\n', '')),
        'fecha_aviso': get_head_attr(pattern=config.reg_ex_head_1, text=td.get_text().replace('\n', '')),
        'nro_aviso': get_head_attr(pattern=config.reg_ex_head_2, text=td.get_text().replace('\n', '')),
        'id_tipo_aviso': get_tipo_aviso(
            get_head_attr(pattern=config.reg_ex_head_3, text=td.get_text().replace('\n', ''))),
        'titulo': encontrarIdTitulo(text),
        'fechaConstitucion': encontrarFechaConstitucion(text),
        'id_titulo': encontrarIdTitulo(text),
        'CUIT': encontrarCUIT(text),
        'capitalSocial': encontrarCapitalSocial(text) if (encontrarCapitalSocial(text) is not None) else 0.00
    }
