from config import Config, reiniciar_config
from db.persistencia import Persistencia
from db.estrategia import Estatregia_Mongo, Estrategia_SQL, Estrategia_Dummy
from model.scrapper import Scrapper
from model.recolector import Recolector
from logger import guardar_log
from helpers.helpers_fechas import obtener_fecha_format
from .mails import MailSender

from tqdm import tqdm


class Controlador:
    def __init__(self, fechas=None):
        self.fechas = [] if not fechas else fechas
        self.setear_fechas_config()

    def setear_fechas_config(self):
        if not self.fechas:
            self.fechas.append(obtener_fecha_format())
            self.fechas.append(obtener_fecha_format())
        Config.PAYLOAD["fechaboletin1"] = obtener_fecha_format(self.fechas[0])
        Config.PAYLOAD["fechaboletin2"] = obtener_fecha_format(self.fechas[1])

    def procesar(self):
        guardar_log(
            "info", f"Inicio de carga - Fecha: {self.fechas[0]} - {self.fechas[1]}"
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
            mensaje = f"Fin de carga \n\n Fecha: ({Config.PAYLOAD['fechaboletin1']} - {Config.PAYLOAD['fechaboletin2']}) - Cantidad registros: {cant_registros}"
            guardar_log(
                "info",
                mensaje,
            )
            mail_sender = MailSender(fecha=obtener_fecha_format())
            mail_sender.enviar_correo(mensaje)
            reiniciar_config()
