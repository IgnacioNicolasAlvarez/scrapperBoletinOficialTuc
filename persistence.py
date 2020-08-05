from abc import abstractmethod
import mysql.connector
from mysql.connector import Error


class Persistence:

    def __init__(self, strategy):
        self._strategy = strategy

    def persist(self, kwargs):
        self._strategy.persist(kwargs)


class Strategy:
    @abstractmethod
    def persist(self, kwargs):
        pass


class StrategyPrintInScreen(Strategy):
    def persist(self, kwargs):
        for key, value in kwargs.items():
            print(f'{key}: {value}')


class StrategyFile(Strategy):
    def __init__(self, filename):
        self.filename = filename

    def persist(self, kwargs):
        file = open(self.filename, "a+")
        file.write("\r\n")
        for key, value in kwargs.items():
            file.write(f'{key}: {value.encode("utf8")} \r')

        file.write("--------------------------------------------------------\r\n")
        file.close()


class StrategyDatabase(Strategy):

    def __init__(self, db_config):
        print(db_config)


    def persist(self, kwargs):
        pass


