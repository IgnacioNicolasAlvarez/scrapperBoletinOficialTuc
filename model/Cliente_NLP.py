from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import Config


class ClienteAzure:
    def __init__(self):
        self.key = Config.AZURE_TA_KEY
        self.endpoint = Config.AZURE_TA_ENDPOINT

    def _autenticar(self):
        credencial = AzureKeyCredential(self.key)
        cliente = TextAnalyticsClient(endpoint=self.endpoint, credential=credencial)
        return cliente

    def extraer_entidades_nombradas(self, texto):
        cliente = self._autenticar()
        try:
            return cliente.recognize_entities(documents=[texto])[0]

        except Exception as err:
            return None
