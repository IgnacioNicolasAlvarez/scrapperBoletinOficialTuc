import sys
import argparse
import datetime
import time

from model.controlador import Controlador
import schedule


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


argumentos_consola = argparse.ArgumentParser(
    prog="app",
    description="Scrapper del Boletín Oficial de la Provincia de Tucumán",
)

argumentos_consola.add_argument(
    "--es_programado", nargs="?", type=str2bool, const=True, default=False
)
argumentos_consola.add_argument(
    "--fecha_desde",
    type=lambda s: datetime.datetime.strptime(s, "%d/%m/%Y"),
    required=False,
)
argumentos_consola.add_argument(
    "--fecha_hasta",
    type=lambda s: datetime.datetime.strptime(s, "%d/%m/%Y"),
    required=False,
)


def job():
    controlador = Controlador()
    controlador.procesar()
    del controlador


# schedule.every().day.at("10:30").do(job)
schedule.every(1).minutes.do(job)


if __name__ == "__main__":
    args = argumentos_consola.parse_args()

    while args.es_programado:
        schedule.run_pending()
        time.sleep(1)

    controlador = Controlador([args.fecha_desde, args.fecha_hasta])
    controlador.procesar()
