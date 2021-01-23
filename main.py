import typer
import schedule
from typing import Optional


from model.controlador import Controlador
from config import Config

import time
from datetime import datetime


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
    fd: Optional[datetime] = typer.Option(None),
    fh: Optional[datetime] = typer.Option(None),
):

    while es_programado:
        schedule.run_pending()
        typer.echo(f"...")
        time.sleep(1)

    controlador = Controlador([fd, fh])
    controlador.procesar()