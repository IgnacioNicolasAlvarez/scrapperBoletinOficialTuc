from config import Config
from helper import get_text_from_aviso
from urlCatcher import get_link_avisos_from_tabla
from persistence import *
import sys


def main(config, dates):

    config.payload['fechaboletin1'] = dates[1]
    # '15/07/2020'
    config.payload['fechaboletin2'] = dates[2]
    # '15/07/2020'
    links = get_link_avisos_from_tabla(config)
    advices = get_text_from_aviso(config, links)

    persistence = Persistence(StrategyPrintInScreen())

    for a in advices:
        persistence.persist(kwargs=a)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(Config, sys.argv)
    else:
        print('Cantidad Incorrecta de Parametros')
