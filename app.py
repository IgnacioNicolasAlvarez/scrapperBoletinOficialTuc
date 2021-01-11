import sys

from helpers.helpers_fechas import obtener_fecha_format
from model.controlador import Controlador


if __name__ == "__main__":

    if len(sys.argv) == 1:
        fechas = [0, obtener_fecha_format(), obtener_fecha_format()]
        controlador = Controlador(fechas)
        controlador.procesar()

    elif len(sys.argv) == 3:
        controlador = Controlador(sys.argv)
        controlador.procesar()
    else:
        print(
            "Cantidad Incorrecta de Parametros. No ingrese ningun parametro para tomar fecha actual o bien ingrese "
            "fecha de inicio y final segun el formato dd/mm/yyyy dd/mm/yyyy"
        )
