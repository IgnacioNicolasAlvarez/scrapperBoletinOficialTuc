from abc import abstractmethod
import mysql.connector
from mysql.connector import Error
from helpers.for_dates import get_date_in_format


class Persistence:

    def __init__(self, strategy):
        self._strategy = strategy

    def persist(self, dictionary):
        self._strategy.persist(dictionary)


class Strategy:
    @abstractmethod
    def persist(self, dictionary):
        pass


class StrategyPrintInScreen(Strategy):
    def persist(self, dictionary):
        for key, value in dictionary.items():
            print(f'{key}: {value}')


class StrategyFile(Strategy):
    def __init__(self, filename):
        self.filename = filename

    def persist(self, dictionary):
        file = open(self.filename, 'a+')
        file.write('\r\n')
        for key, value in dictionary.items():
            file.write(f'{key}: {value.encode("utf8")} \r')

        file.write('--------------------------------------------------------\r\n')
        file.close()


class StrategyDatabase(Strategy):

    def __init__(self, db_config):
        self.host = db_config['DB_HOST']
        self.name = db_config['DB_NAME']
        self.user = db_config['DB_USER']
        self.password = db_config['DB_PASS']
        self.port = db_config['DB_PORT']

    def persist(self, dictionary):
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
                                '{get_date_in_format(dictionary['fecha_aviso'])}',
                                '{dictionary['nro_aviso']}',
                                '{dictionary['id_tipo_aviso']}',
                                '{dictionary['CUIT']}', 
                                '{dictionary['razon_social']}', 
                                '{dictionary['fechaConstitucion']}',
                                '{dictionary['id_titulo']}',
                                '{dictionary['id_tipo_sociedad']}',
                                '{dictionary['capitalSocial']}',
                                '{dictionary['texto']}',
                                sysdate()
                                );
                    """
                cursor.execute(query)
                connection.commit()

        except Error as e:
            print('Error en conexion con BD.')
        finally:
            if connection.is_connected():
                cursor.close()
                connection.rollback()
                connection.close()
