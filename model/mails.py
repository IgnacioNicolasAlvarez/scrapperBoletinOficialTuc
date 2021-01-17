from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from config import Config


class MailSender:
    def __init__(self, fecha):
        self.fecha = fecha

    def enviar_correo(self):
       pass

    def setear_asunto(self):
        return Config.MAIL["MAIL_ASUNTO"] + " - " + self.fecha
