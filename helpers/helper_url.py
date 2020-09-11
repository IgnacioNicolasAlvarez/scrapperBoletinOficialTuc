import requests
from bs4 import BeautifulSoup
from helpers.d_wait import wait
from config import Config

class RecolectorUrls:

    def __init__(self):
        self.flag_ultima_hoja = True


    def get_urls(self):
        links = []
        url_base = Config.URLS['tabla_url']
        headers = Config.headers
        params = Config.payload.copy()

        while True:
            urls_or_none = self.get_urls_2(url_base, headers, params)
            
            if urls_or_none is None:
                break

            links.extend(urls_or_none)
            params['offset'] += Config.offset_increment
        return links


    @wait(1)
    def get_urls_2(self, url_tabla, headers, payload):
        response = requests.get(url_tabla, headers=headers, params=payload)
        bs = BeautifulSoup(response.text, 'html.parser')
        a_tag_list = bs.find_all("a", href=True)

        existe_ultimo = bs.find("img", {'src': 'images/ultimo.gif'})

        if existe_ultimo is None:
            if self.flag_ultima_hoja:
                self.flag_ultima_hoja = False
            else:
                return None
        return [a_tag['href'] for a_tag in a_tag_list if a_tag['href'].startswith('aviso')]
