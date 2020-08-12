from config import Config
from helpers.helper import get_dic_from_urls
from scrapper.urlCatcher import get_urls_avisos_from_tabla
from db.persistence import *
import sys


def main(config, dates):

    config.payload['fechaboletin1'] = dates[1]
    # '15/07/2020'
    config.payload['fechaboletin2'] = dates[2]
    # '15/07/2020'
    urls = get_urls_avisos_from_tabla(config)
    advices = get_dic_from_urls(config, urls)

    persistence = Persistence(StrategyPrintInScreen())

    for a in advices:
        persistence.persist(kwargs=a)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(Config, sys.argv)
    else:
        print('Cantidad Incorrecta de Parametros')
