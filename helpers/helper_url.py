import requests
from bs4 import BeautifulSoup
from helpers.d_wait import wait
from config import Config


class RecolectorUrls:

    def __init__(self):
        self.flag_ultima_hoja = True

    def get_urls(self, headers, params):
        links = []
        url_base = Config.URLS['tabla_url']

        while True:
            urls_or_none = self._get_urls(url_base, headers, params)

            if urls_or_none is None:
                break

            links.extend(urls_or_none)
            params['offset'] += Config.offset_increment
        return links

    @wait(3)
    def _get_urls(self, url_tabla, headers, payload):
        response = requests.get(url_tabla, headers=headers, params=payload)
        bs = BeautifulSoup(response.text, 'html.parser')
        a_tag_list = bs.find_all("a", href=True)

        existe_ultimo = bs.find("img", {'src': 'images/ultimo.gif'})

        if existe_ultimo is None:
            if self.flag_ultima_hoja:
                self.flag_ultima_hoja = False
            else:
                return None
        return [a['href'] for a in a_tag_list if a['href'].startswith('aviso')]
