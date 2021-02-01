from config import Config
from helpers.expresionesRegularesF import (
    encontrarCapitalSocial,
    encontrarCUIT,
    encontrarFechaConstitucion,
    encontrarIdTitulo,
    encontrarTipoSociedad,
    get_razon_social,
    get_razon_social_aviso,
)
from helpers.for_categorias import get_tipo_categoria
from helpers.helper import get_feature_from_tittle
from helpers.helpers_fechas import obtener_fecha_format

from model.IA import NLP

from .aviso import Aviso


class Aviso_Factory:
    def __init__(self):
        self.nlp = NLP()

    def crear_aviso(self, datos_raw):
        texto, header = datos_raw

        diccionario_aviso = dict()
        diccionario_aviso["texto"] = texto

        diccionario_aviso["nro_boletin"] = get_feature_from_tittle(
            pattern=Config.REGEX_HEADER_0, text=header
        )
        diccionario_aviso["fecha_aviso"] = obtener_fecha_format(
            get_feature_from_tittle(pattern=Config.REGEX_HEADER_1, text=header)
        )
        diccionario_aviso["nro_aviso"] = get_feature_from_tittle(
            pattern=Config.REGEX_HEADER_2, text=header
        )
        diccionario_aviso["id_tipo_aviso"] = get_tipo_categoria(
            get_feature_from_tittle(pattern=Config.REGEX_HEADER_3, text=header)
        )
        diccionario_aviso["razon_social"] = get_razon_social_aviso(
            text=texto, header=header
        )
        diccionario_aviso["id_tipo_sociedad"] = encontrarTipoSociedad(header)
        diccionario_aviso["titulo"] = encontrarIdTitulo(texto)
        diccionario_aviso["fechaConstitucion"] = encontrarFechaConstitucion(texto)
        diccionario_aviso["id_titulo"] = encontrarIdTitulo(texto)
        diccionario_aviso["CUIT"] = encontrarCUIT(texto)

        diccionario_aviso["capitalSocial"] = self.nlp.extraer_capital_social(
            pregunta="¿monto capital social?",
            texto=texto.replace(".", "").lower(),
        )
        
        diccionario_aviso["fecha_carga"] = obtener_fecha_format()

        return self._crear_aviso(diccionario_aviso)

    def _aplicar_encoding(self, t):
        return t.encode("ascii", "ignore").decode()

    def _crear_aviso(self, diccionario):
        return Aviso(diccionario=diccionario)
