import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from model.aviso import Aviso
from helpers.expresionesRegularesF import *
from helpers.for_categorias import isCategoriaRequerida
from helpers import helper
from helpers.d_wait import wait
from config import Config
from logger import Logger


class Extractor:
    @wait(3)
    def extraer_datos_urls(self, links):
        textos_y_encabezados = []

        for link in links:
            link = Config.URLS["base_url"] + link
            response = requests.get(link, headers=Config.HEADERS)
            bs = BeautifulSoup(response.text, "html.parser")
            tr = bs.find_all("tr", {"valign": "middle"})

            text = self._get_aviso_text(bs)

            for td in tr:
                texto_header = self._limpiar_header(td)
                descripcion_aviso = helper.get_feature_from_tittle(
                    pattern=Config.REGEX_HEADER_3, text=texto_header
                )

                if isCategoriaRequerida(descripcion_aviso) and (
                    self._es_aviso_baneado(text) or self._es_aviso_baneado(texto_header)
                ):
                    textos_y_encabezados.append((text, texto_header))

        return textos_y_encabezados

    def _limpiar_header(self, td):
        text = td.get_text()
        text = text.replace("\n", "")
        text = text.replace("”", "")
        return text

    def _es_aviso_baneado(self, text):
        for ban in Config.BAN_SOCIEDADES:
            if ban in text:
                return False
        return True

    def _get_aviso_text(self, bs):
        texto_aviso = None
        try:
            main_text = bs.find_all("tr", {"bgcolor": "#E4ECED"})
            texto_aviso = main_text[1].find_all("p")[1].get_text()
        except Exception as e:
            Logger.guardar_log("error", "Extraer info de aviso")

        return texto_aviso
