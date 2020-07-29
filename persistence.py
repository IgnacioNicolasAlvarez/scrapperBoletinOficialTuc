from abc import abstractmethod
import boto3


class Persistence:

    def __init__(self, strategy):
        self._strategy = strategy

    def persist(self):
        self._strategy.persist()


class Strategy:
    @abstractmethod
    def persist(self):
        pass


class StrategyFile(Strategy):
    def persist(self):
        pass

