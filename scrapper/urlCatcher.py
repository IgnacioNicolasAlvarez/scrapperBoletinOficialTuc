import requests
from bs4 import BeautifulSoup


def get_urls_avisos_from_tabla(config):
    response = requests.get(config.URLS['tabla_url'], headers=config.headers, params=config.payload)
    bs = BeautifulSoup(response.text, 'html.parser')
    a_tag_list = bs.find_all("a", href=True)

    links = [a_tag['href'] for a_tag in a_tag_list if a_tag['href'].startswith('aviso')]
    return links
