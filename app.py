from config import Config
from helpers.helper import get_dic_from_urls
from scrapper.urlCatcher import get_urls_avisos_from_tabla
from helpers.for_dates import get_current_format_date
from db.persistence import *
import sys


def main(config, dates):
    config.payload['fechaboletin1'] = dates[1]
    # '15/07/2020'
    config.payload['fechaboletin2'] = dates[2]
    # '15/07/2020'
    urls = get_urls_avisos_from_tabla(config)
    advices = get_dic_from_urls(config, urls)

    persistence = Persistence(StrategyDatabase(Config.DB_DOCKER))
    for a in advices:
        persistence.persist(dictionary=a)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        dates = [0, get_current_format_date(), get_current_format_date()]
        main(Config, dates)

    elif len(sys.argv) == 3:
        main(Config, sys.argv)
    else:
        print('Cantidad Incorrecta de Parametros')
