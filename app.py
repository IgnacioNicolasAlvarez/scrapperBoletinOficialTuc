import sys

from config import Config
from helpers.helper_url import RecolectorUrls
from helpers.for_dates import get_current_format_date
from db.persistence import Persistence, StrategyMongo, StrategyPrintInScreen
from scrapper.scrapper import Scrapper
from logger import guardar_log

from tqdm import tqdm


def main(dates):

    guardar_log("info", f"Inicio de carga - Fecha: {dates[1]} - {dates[2]}")

    Config.payload["fechaboletin1"] = dates[1]
    Config.payload["fechaboletin2"] = dates[2]

    print("Empezando recoleccion de URLs")

    recolector = RecolectorUrls()
    urls = recolector.get_urls(Config.headers, Config.payload)

    print("Empezando extraccion de datos de Avisos")
    scrapper = Scrapper()
    avisos = scrapper.extract_data(urls)

    print("Empezando Almacenamiento de datos en BD")
    try:
        persistence = Persistence(
            [
                # StrategyPrintInScreen(),
                StrategyMongo(Config.DB_MONGO),
                # StrategyDatabase(Config.DB_PROD)
            ]
        )
        for a in tqdm(avisos):
            persistence.persist(a)
    except Exception as e:
        print(f"Error app: {e}")

    finally:
        print("Fin del proceso")
        guardar_log("info", f"Fin de carga - Fecha: {dates[1]} - {dates[2]}")


if __name__ == "__main__":

    if len(sys.argv) == 1:
        dates = [0, get_current_format_date(), get_current_format_date()]
        main(dates)

    elif len(sys.argv) == 3:
        main(sys.argv)
    else:
        print(
            "Cantidad Incorrecta de Parametros. No ingrese ningun parametro para tomar fecha actual o bien ingrese "
            "fecha de inicio y final segun el formato dd/mm/yyyy dd/mm/yyyy"
        )
