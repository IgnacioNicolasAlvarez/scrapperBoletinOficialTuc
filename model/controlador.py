from config import Config
from db.persistencia import (
    Persistencia,
    Estatregia_Mongo,
    Estrategia_SQL,
    Estrategia_Dummy,
)
from model.scrapper import Scrapper
from model.recolector import Recolector
from logger import guardar_log

from tqdm import tqdm


class Controlador:
    def __init__(self, fechas):
        self.fechas = fechas
        self.setear_fechas_config()

    def setear_fechas_config(self):
        Config.PAYLOAD["fechaboletin1"] = self.fechas[1]
        Config.PAYLOAD["fechaboletin2"] = self.fechas[2]

    def procesar(self):
        guardar_log(
            "info", f"Inicio de carga - Fecha: {self.fechas[1]} - {self.fechas[2]}"
        )

        print("Empezando recoleccion de URLs")

        recolector = Recolector()
        urls = recolector.obtener_urls(Config.headers, Config.PAYLOAD)

        print("Empezando extraccion de datos de Avisos")
        scrapper = Scrapper()
        avisos = scrapper.extraer_datos_urls(urls)

        print("Empezando Almacenamiento de datos en BD")
        try:
            persistencia = Persistencia(
                [
                    Estrategia_Dummy(),
                    # Estatregia_Mongo(Config.DB_MONGO),
                    # Estrategia_SQL(Config.DB_PROD)
                ]
            )
            cant_registros = 0
            for a in tqdm(avisos):
                cant_registros += persistencia.persistir(a)
        except Exception as e:
            guardar_log("error", f"Persistiendo Aviso - Error: {e}")

        finally:
            print("Fin del proceso")
            guardar_log(
                "info",
                f"Fin de carga - Fecha: ({self.fechas[1]} - {self.fechas[2]}) - Cantidad registros: {cant_registros}",
            )
