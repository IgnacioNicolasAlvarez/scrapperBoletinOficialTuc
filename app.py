import sys

from config import Config
from helpers.helper_url import RecolectorUrls
from helpers.for_dates import get_current_format_date
from db.persistence import *
from scrapper.scrapper import Scrapper


def main(dates):
    Config.payload['fechaboletin1'] = dates[1]
    Config.payload['fechaboletin2'] = dates[2]

    print("Empezando recoleccion de URLs")
    urls = RecolectorUrls().get_urls()

    print("Empezando extraccion de datos de Avisos")
    avisos = Scrapper().extract_data(urls)

    print("Empezando Almacenamiento de datos en BD")
    try:
        persistence = Persistence(StrategyDatabase(Config.DB_DOCKER))
        for a in avisos:
            persistence.persist(dictionary=a)
    except Exception as e:
        print("Error: Falla en comunicacion con BD.")
    print("Fin del proceso.")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        dates = [0, get_current_format_date(), get_current_format_date()]
        main(dates)

    elif len(sys.argv) == 3:
        main(sys.argv)
    else:
        print(
            'Cantidad Incorrecta de Parametros. No ingrese ningun parametro para tomar fecha actual o bien ingrese fecha de inicio y final segun el formato dd/mm/yyyy dd/mm/yyyy')
