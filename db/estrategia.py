from abc import abstractmethod

import mysql.connector
from logger import Logger
from mysql.connector import Error
from pymongo import MongoClient


class Estrategia:
    @abstractmethod
    def persistir(self, aviso):
        return 0

    @abstractmethod
    def resetar_fecha(self, fechas):
        pass


class Estrategia_Dummy(Estrategia):
    def persistir(self, aviso):
        return 1

    def resetar_fecha(self, fechas):
        print("Reseteando la fecha")


class Estatregia_Mongo(Estrategia):
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client.Boletin

    def persistir(self, aviso):

        try:
            self.db.aviso.insert_one(aviso.__dict__)
            return 1
        except Exception as e:
            Logger.guardar_log(
                "error", f"Conexion insert en MongoDB - Aviso: {aviso.nro_aviso}"
            )
            return 0

    def resetar_fecha(self, fechas):

        try:
            query = {"fecha_carga": {"$gt": f"{fechas[0]}", "$lt": f"{fechas[1]}"}}
            self.db.aviso.delete_many(query)
        except Exception as e:
            Logger.guardar_log(
                "error", f"Delete entre fechas en MongoDB - Query: {query}"
            )

    def __del__(self):
        self.client.close()


class Estrategia_SQL(Estrategia):
    def __init__(self, db_config):
        self.connection = mysql.connector.connect(
            host=db_config["DB_HOST"],
            database=db_config["DB_NAME"],
            user=db_config["DB_USER"],
            password=db_config["DB_PASS"],
        )
        self.cursor = self.connection.cursor()
        
    def persistir(self, aviso):
        registro_insertado = 0
        try:
            
            if self.connection.is_connected():
                query = f"""
                        insert into auxiliar_tuc 
                        (id_provincia, fecha_publicacion, boletin, id_categoria, cuit, razon_social, 
                        fecha_constitucion_soc, id_titulo, id_tpublicacion_soc, capita_social, texto, fecha) 
                        values (
                                '{1}',
                                '{aviso.fecha_aviso}',
                                '{aviso.nro_boletin}',
                                '{aviso.id_tipo_aviso}',
                                '{aviso.CUIT}', 
                                '{aviso.razon_social}', 
                                '{aviso.fechaConstitucion}',
                                '{aviso.id_titulo}',
                                '{aviso.id_tipo_sociedad}',
                                '{aviso.capitalSocial}',
                                '{aviso.texto}',
                                sysdate()
                                );
                    """
                self.cursor.execute(query)
                self.connection.commit()
                registro_insertado = 1

        except Error as e:
            Logger.guardar_log(
                "error", f"Conexion insert en SQL - Aviso: {aviso.nro_aviso}"
            )

        return registro_insertado

    def resetar_fecha(self, fechas):
        try:
            if self.connection.is_connected():
                query = f"""
                        delete auxiliar_tuc where 
                        fecha between '{fechas[0]}' and '{fechas[1]}';
                    """
                self.cursor.execute(query)
                self.connection.commit()

        except Error as e:
            Logger.guardar_log("error", f"Delete entre fechas en MongoDB")

    def __del__(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()