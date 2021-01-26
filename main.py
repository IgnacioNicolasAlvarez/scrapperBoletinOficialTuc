import time
from datetime import datetime
from typing import Optional

import schedule
import typer

from config import Config
from model.controlador import Controlador


def job():
    controlador = Controlador()
    controlador.procesar()
    del controlador


# schedule.every().day.at(Config.HORA_EJECUCION).do(job)
schedule.every(1).minutes.do(job)


def main(
    es_programado: bool = typer.Argument(
        False, help="Es Programado? True/False", show_default=True
    ),
    es_resetear_fecha: bool = typer.Argument(
        False, help="Es Resetear Fecha? True/False", show_default=True
    ),
    fd: Optional[datetime] = typer.Option(None),
    fh: Optional[datetime] = typer.Option(None),
):

    while es_programado:
        schedule.run_pending()
        typer.echo(f"...")
        time.sleep(1)

    controlador = Controlador(fechas=[fd, fh], es_resetear_fecha=es_resetear_fecha)
    controlador.procesar()
