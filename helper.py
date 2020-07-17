import requests
from bs4 import BeautifulSoup
from helper_regex import get_head_attr

def get_link_avisos_from_tabla(config):
    response = requests.get(config.tabla_url, headers=config.headers, params=config.payload)
    bs = BeautifulSoup(response.text, 'html.parser')
    a_tag_list = bs.find_all("a", href=True)

    links = [a_tag['href'] for a_tag in a_tag_list if a_tag['href'].startswith('aviso')]
    return links


def get_text_from_aviso(config, link):
    link = config.base_url + link

    response = requests.get(link, headers=config.headers)
    bs = BeautifulSoup(response.text, 'html.parser')
    tr = bs.find_all("tr", {'valign' : 'middle'})

    head = [td.get_text().replace('\n', '') for td in tr]
    print(get_head_attr(pattern=config.reg_ex_head, text=head[0]))







