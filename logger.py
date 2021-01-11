import logging
import datetime

logging.basicConfig(
    filename="./logs/app.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def guardar_log(level, message):

    if level.lower() == "error":
        logging.warning(message)
    elif level.lower() == "info":
        logging.info(message)