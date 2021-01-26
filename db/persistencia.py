from time import sleep


class Persistencia:
    def __init__(self, estrategias):
        self.estrategias = estrategias

    def persistir(self, aviso):
        sleep(0.10)
        cant_registros = 0
        for estrategia in self.estrategias:
            cant_registros += estrategia.persistir(aviso)
        return cant_registros

    def resetar_fecha(self, fechas):
        for estrategia in self.estrategias:
            estrategia.resetar_fecha(fechas)