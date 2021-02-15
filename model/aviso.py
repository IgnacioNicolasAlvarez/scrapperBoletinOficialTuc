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


class Aviso:
    def __init__(self, diccionario):

        self.texto = diccionario["texto"]
        self.nro_boletin = diccionario["nro_boletin"]
        self.fecha_aviso = diccionario["fecha_aviso"]
        self.nro_aviso = diccionario["nro_aviso"]
        self.id_tipo_aviso = diccionario["id_tipo_aviso"]
        self.razon_social = diccionario["razon_social"]
        self.id_tipo_sociedad = diccionario["id_tipo_sociedad"]
        self.titulo = diccionario["titulo"]
        self.fechaConstitucion = diccionario["fechaConstitucion"]
        self.id_titulo = diccionario["id_titulo"]
        self.CUIT = diccionario["CUIT"]
        self.fecha_carga = diccionario["fecha_carga"]
        self.capitalSocial = diccionario["capitalSocial"]
        self.nombres = diccionario["nombres"]
        self.direccion = diccionario["direccion"]

    def __str__(self):
        return self.nombre_razon_social + "\n\n" + self.capitalSocial
