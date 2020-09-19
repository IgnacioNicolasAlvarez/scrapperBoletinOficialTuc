from config import Config
from helpers.expresionesRegularesF import encontrarTipoSociedad, get_razon_social, encontrarIdTitulo, \
    encontrarFechaConstitucion, encontrarCUIT, encontrarCapitalSocial
from helpers.for_categorias import get_tipo_categoria
from helpers.for_dates import get_date_in_format
from helpers.helper import get_feature_from_tittle


class Aviso:
    def __init__(self, text, td):
        if text:
            self.texto = text
            self.nro_boletin = get_feature_from_tittle(pattern=Config.reg_ex_head_0,
                                                       text=td.get_text().replace('\n', ''))
            self.fecha_aviso = get_date_in_format(
                get_feature_from_tittle(pattern=Config.reg_ex_head_1, text=td.get_text().replace('\n', '')))
            self.nro_aviso = get_feature_from_tittle(pattern=Config.reg_ex_head_2, text=td.get_text().replace('\n', ''))
            self.id_tipo_aviso = get_tipo_categoria(
                get_feature_from_tittle(pattern=Config.reg_ex_head_3, text=td.get_text().replace('\n', '')))
            self.razon_social = get_razon_social(td.get_text().replace('\n', ''))
            self.id_tipo_sociedad = encontrarTipoSociedad(text)
            self.titulo = encontrarIdTitulo(text)
            self.fechaConstitucion = encontrarFechaConstitucion(text)
            self.id_titulo = encontrarIdTitulo(text)
            self.CUIT = encontrarCUIT(text)
            self.capitalSocial = encontrarCapitalSocial(text[:-30]) if (
                    encontrarCapitalSocial(text) is not None) else 0.00
