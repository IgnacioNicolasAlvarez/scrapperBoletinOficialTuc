import requests
from bs4 import BeautifulSoup
from helpers.d_wait import wait


def get_urls_avisos_from_tabla(config):
    links = []
    url_base = config.URLS['tabla_url']
    headers = config.headers
    params = config.payload.copy()

    while True:
        urls_or_none = get_urls(url_base, headers, params)

        if urls_or_none is None:
            break

        links.extend(urls_or_none)
        params['offset'] += config.offset_increment
    return links


@wait(1)
def get_urls(url_tabla, headers, payload):
    response = requests.get(url_tabla, headers=headers, params=payload)
    bs = BeautifulSoup(response.text, 'html.parser')
    a_tag_list = bs.find_all("a", href=True)

    existe_ultimo = bs.find("img", {'src': 'images/ultimo.gif'})

    if existe_ultimo is None:
        return None
    return [a_tag['href'] for a_tag in a_tag_list if a_tag['href'].startswith('aviso')]
