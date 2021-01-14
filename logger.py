import logging
import datetime

logging.basicConfig(
    filename="./logs/app.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)



def guardar_log(nivel, mensaje):

    if nivel.lower() == "info":
        logging.info(mensaje)
    else:
        logging.warning(mensaje)
