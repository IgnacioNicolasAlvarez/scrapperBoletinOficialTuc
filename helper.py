import requests
from bs4 import BeautifulSoup
from helper_regex import get_head_attr


def get_link_avisos_from_tabla(config):
    response = requests.get(config.tabla_url, headers=config.headers, params=config.payload)
    bs = BeautifulSoup(response.text, 'html.parser')
    a_tag_list = bs.find_all("a", href=True)

    links = [a_tag['href'] for a_tag in a_tag_list if a_tag['href'].startswith('aviso')]
    return links


def _get_text_from_aviso(bs):
    main_text = bs.find_all("tr", {'bgcolor': '#E4ECED'})
    return main_text[1].find_all('p')[1].get_text()


def get_text_from_aviso(config, links):
    aviso = []

    for link in links:
        link = config.base_url + link
        response = requests.get(link, headers=config.headers)
        bs = BeautifulSoup(response.text, 'html.parser')
        tr = bs.find_all("tr", {'valign': 'middle'})

        for td in tr:
            aviso.append({
                'text': _get_text_from_aviso(bs),
                'header': get_head_attr(pattern=config.reg_ex_head, text=td.get_text().replace('\n', ''))
            })

    return aviso
