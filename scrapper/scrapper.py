import requests
from bs4 import BeautifulSoup

from Model.model import Aviso
from helpers.expresionesRegularesF import *
from helpers.for_categorias import get_tipo_categoria, isCategoriaRequerida
from helpers import helper
from helpers.d_wait import wait
from config import Config


class Scrapper:

    @wait(3)
    def extract_data(self, links):
        lista_avisos = []

        for link in links:
            link = Config.URLS['base_url'] + link
            response = requests.get(link, headers=Config.headers)
            bs = BeautifulSoup(response.text, 'html.parser')
            tr = bs.find_all("tr", {'valign': 'middle'})

            text = self._get_aviso_text(bs)
            for td in tr:
                texto_header = self._limpiar_header(td)
                descripcion_aviso = helper.get_feature_from_tittle(pattern=Config.reg_ex_head_3,
                                                                   text=texto_header)
                if isCategoriaRequerida(descripcion_aviso):
                    if es_razon_social_solicitada(texto_header):
                        print(descripcion_aviso)
                        lista_avisos.append(Aviso(text, texto_header))

        return lista_avisos

    def _limpiar_header(self, td):
        text = td.get_text()
        text = text.replace('\n', '')
        text = text.replace('”', '')
        return text

    def _get_aviso_text(self, bs):
        try:
            main_text = bs.find_all("tr", {'bgcolor': '#E4ECED'})
            return main_text[1].find_all('p')[1].get_text()
        except Exception as e:
            print(f'Error: Extraer info de aviso - {e}')
            return None
