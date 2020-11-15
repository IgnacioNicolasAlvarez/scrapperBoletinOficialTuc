from abc import abstractmethod

import mysql.connector
from mysql.connector import Error
from pymongo import MongoClient


class Persistence:

    def __init__(self, strategies):
        self._strategies = strategies

    def persist(self, aviso):
        for strategy in self._strategies:
            strategy.persist(aviso)


class Strategy:
    @abstractmethod
    def persist(self, aviso):
        pass


class StrategyPrintInScreen(Strategy):
    def persist(self, aviso):
        print(aviso.__dict__)


class StrategyMongo(Strategy):
    def __init__(self, uri):
        self.conection_str = uri

    def persist(self, aviso):
        client = MongoClient(self.conection_str)
        db = client.Boletin
        try:
            db.aviso.insert_one(aviso.__dict__)
        except Exception as e:
            print(e)
            pass


class StrategyDatabase(Strategy):

    def __init__(self, db_config):
        self.host = db_config['DB_HOST']
        self.name = db_config['DB_NAME']
        self.user = db_config['DB_USER']
        self.password = db_config['DB_PASS']
        self.port = db_config['DB_PORT']

    def persist(self, aviso):
        connection = mysql.connector.connect()
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.name,
                                                 user=self.user,
                                                 password=self.password,
                                                 port=self.port)
            if connection.is_connected():
                cursor = connection.cursor()
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
                cursor.execute(query)
                connection.commit()

        except Error as e:
            print(aviso)
            print(f'Error en insert con BD: {e} ')
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.rollback()
                connection.close()
