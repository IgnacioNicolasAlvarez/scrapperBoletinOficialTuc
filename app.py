from config import Config
from scrapper.scrapper import extract_data
from helpers.helper_url import get_urls
from helpers.for_dates import get_current_format_date
from db.persistence import *
import sys


def main(dates):
    Config.payload['fechaboletin1'] = dates[1]
    Config.payload['fechaboletin2'] = dates[2]
    urls = get_urls()
    advices = extract_data(urls)

    persistence = Persistence(StrategyDatabase(Config.DB_PROD))
    for a in advices:
        persistence.persist(dictionary=a)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        dates = [0, get_current_format_date(), get_current_format_date()]
        main(dates)

    elif len(sys.argv) == 3:
        main(sys.argv)
    else:
        print('Cantidad Incorrecta de Parametros')
