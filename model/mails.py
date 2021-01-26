import yagmail
from config import Config


class MailSender:
    def __init__(self, fecha):
        self.fecha = fecha

    def enviar_correo(self, mensaje):
        yagmail.register(Config.MAIL["MAIL_USUARIO"], Config.MAIL["MAIL_PASS"])

        with yagmail.SMTP(Config.MAIL["MAIL_USUARIO"]) as yag:
            yag.send(
                to=Config.MAIL["MAIL_DESTINO"],
                subject=self.setear_asunto(),
                contents=mensaje,
            )

    def setear_asunto(self):
        return Config.MAIL["MAIL_ASUNTO"] + " - " + self.fecha
