import requests
from bs4 import BeautifulSoup
from helpers.expresionesRegularesF import *
from helpers.for_sociedades import get_tipo_sociedad
from helpers.for_categorias import get_tipo_categoria
from helpers.d_wait import wait
from config import Config


def get_feature_from_tittle(pattern, text):
    x = []
    try:
        x = re.findall(pattern, text)[0]
    except Exception as e:
        print(f'Error: {e}, Pattern: {pattern}, Text: {text}')
    return x


def _get_aviso_text(bs):
    main_text = None
    try:
        main_text = bs.find_all("tr", {'bgcolor': '#E4ECED'})
        return main_text[1].find_all('p')[1].get_text()
    except Exception as e:
        print(main_text)
        return None


@wait(1)
def extract_data(links):
    aviso = []

    for link in links:
        link = Config.URLS['base_url'] + link
        response = requests.get(link, headers=Config.headers)
        bs = BeautifulSoup(response.text, 'html.parser')
        tr = bs.find_all("tr", {'valign': 'middle'})

        text = _get_aviso_text(bs)
        for td in tr:
            descripcion_aviso = get_feature_from_tittle(pattern=Config.reg_ex_head_3,
                                                        text=td.get_text().replace('\n', ''))
            if isCategoriaRequerida(descripcion_aviso):
                aviso.append(create_dic(text, td))

    return aviso


def isCategoriaRequerida(text):
    for cat in Config.reg_categorias_solicitadas:
        if cat in text:
            return True
    return False


def create_dic(text, td):
    if text:
        return {
            'texto': text.replace("'", " "),
            'nro_boletin': get_feature_from_tittle(pattern=Config.reg_ex_head_0, text=td.get_text().replace('\n', '')),
            'fecha_aviso': get_feature_from_tittle(pattern=Config.reg_ex_head_1, text=td.get_text().replace('\n', '')),
            'nro_aviso': get_feature_from_tittle(pattern=Config.reg_ex_head_2, text=td.get_text().replace('\n', '')),
            'id_tipo_aviso': get_tipo_categoria(
                get_feature_from_tittle(pattern=Config.reg_ex_head_3, text=td.get_text().replace('\n', ''))),
            'razon_social': get_razon_social(td.get_text().replace('\n', '')),
            'id_tipo_sociedad': encontrarTipoSociedad(text),
            'titulo': encontrarIdTitulo(text),
            'fechaConstitucion': encontrarFechaConstitucion(text),
            'id_titulo': encontrarIdTitulo(text),
            'CUIT': encontrarCUIT(text),
            'capitalSocial': encontrarCapitalSocial(text[:-30]) if (encontrarCapitalSocial(text) is not None) else 0.00
        }
    return None
