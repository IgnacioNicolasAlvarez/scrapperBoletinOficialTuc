import typer
from config import Config, reiniciar_config
from db.estrategia import Estatregia_Mongo, Estrategia_Dummy, Estrategia_SQL
from db.persistencia import Persistencia
from helpers.helpers_fechas import obtener_fecha_format
from logger import Logger
from tqdm import tqdm

from model.extractor import Extractor
from model.recolector import Recolector
from model.factory import Aviso_Factory

from .mails import MailSender


class Controlador:
    def __init__(self, fechas=None, es_resetear_fecha=False):
        self.fechas = [] if not fechas else fechas
        self.es_resetear_flag = es_resetear_fecha
        self.setear_fechas_config()

    def setear_fechas_config(self):
        if not self.fechas:
            self.fechas.append(obtener_fecha_format())
            self.fechas.append(obtener_fecha_format())
        Config.PAYLOAD["fechaboletin1"] = obtener_fecha_format(self.fechas[0])
        Config.PAYLOAD["fechaboletin2"] = obtener_fecha_format(self.fechas[1])

    def procesar(self):
        Logger.guardar_log(
            "info", f"Inicio de carga - Fecha: {self.fechas[0]} - {self.fechas[1]}"
        )

        typer.secho("Empezando recoleccion de URLs", fg=typer.colors.GREEN)
        recolector = Recolector()
        urls = recolector.obtener_urls(Config.HEADERS, Config.PAYLOAD)

        typer.secho("Empezando extraccion de datos de Avisos", fg=typer.colors.GREEN)
        extractor = Extractor()
        datos_raw = extractor.extraer_datos_urls(urls)

        factory = Aviso_Factory()
        avisos = [factory.crear_aviso(raw_i) for raw_i in datos_raw]

        typer.secho("Empezando Almacenamiento de datos en BD", fg=typer.colors.GREEN)
        try:
            persistencia = Persistencia(
                [
                    Estrategia_Dummy(),
                    # Estatregia_Mongo(Config.DB_MONGO),
                    # Estrategia_SQL(Config.DB_PROD)
                ]
            )
            if self.es_resetear_flag:
                persistencia.resetar_fecha(self.fechas)

            cant_registros = 0

            for a in tqdm(avisos):
                cant_registros += persistencia.persistir(a)

        except Exception as e:
            Logger.guardar_log("error", f"Persistiendo Aviso - Error: {e}")

        finally:
            typer.secho("Fin del proceso", fg=typer.colors.BRIGHT_GREEN)
            mensaje = f"Fin de carga \n\n Fecha: ({Config.PAYLOAD['fechaboletin1']} - {Config.PAYLOAD['fechaboletin2']}) - Cantidad registros: {cant_registros}"
            Logger.guardar_log(
                "info",
                mensaje,
            )
            mail_sender = MailSender(fecha=obtener_fecha_format())
            mail_sender.enviar_correo(mensaje)
            reiniciar_config()
