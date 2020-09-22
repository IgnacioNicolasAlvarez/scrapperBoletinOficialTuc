from config import Config
from helpers.expresionesRegularesF import encontrarTipoSociedad, get_razon_social, encontrarIdTitulo, \
    encontrarFechaConstitucion, encontrarCUIT, encontrarCapitalSocial
from helpers.for_categorias import get_tipo_categoria
from helpers.for_dates import get_date_in_format
from helpers.helper import get_feature_from_tittle


class Aviso:
    def __init__(self, text, header_text):
        self.texto = text
        self.nro_boletin = get_feature_from_tittle(pattern=Config.reg_ex_head_0,
                                                   text=header_text)
        self.fecha_aviso = get_date_in_format(
            get_feature_from_tittle(pattern=Config.reg_ex_head_1, text=header_text))
        self.nro_aviso = get_feature_from_tittle(pattern=Config.reg_ex_head_2, text=header_text)
        self.id_tipo_aviso = get_tipo_categoria(
            get_feature_from_tittle(pattern=Config.reg_ex_head_3, text=header_text))
        self.razon_social = get_razon_social(header_text)
        self.id_tipo_sociedad = encontrarTipoSociedad(header_text)
        self.titulo = encontrarIdTitulo(text)
        self.fechaConstitucion = encontrarFechaConstitucion(text)
        self.id_titulo = encontrarIdTitulo(text)
        self.CUIT = encontrarCUIT(text)
        self.capitalSocial = encontrarCapitalSocial(text[:-30]) if (
                encontrarCapitalSocial(text) is not None) else 0.00

    def __str__(self):
        return self.razon_social
