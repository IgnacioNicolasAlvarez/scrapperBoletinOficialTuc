from config import Config
from helper import get_link_avisos_from_tabla, get_text_from_aviso


def main(config):

    config.payload['fechaboletin1'] = '15/07/2020'
    config.payload['fechaboletin2'] = '15/07/2020'

    links = get_link_avisos_from_tabla(config)
    get_text_from_aviso(config, links[0])


if __name__ == '__main__':
    main(Config)
