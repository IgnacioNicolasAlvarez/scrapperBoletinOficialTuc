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

    def extraer_entidades(self, texto):
        cliente = self._autenticar()
        try:
            # is_error = False
            return cliente.recognize_entities(documents=[texto])[0].entities
        except Exception as err:
            return None

    def extraer_capital_social(self, entidades):
        capital_social = 0
        for ent in entidades:
            if ent.category == "Quantity" and ent.subcategory == "Currency":
                if "$" in ent.text:
                    aux = float(ent.text.replace("$", ""))
                    capital_social = (
                        aux if aux > capital_social and aux > 5000 else capital_social
                    )
        return capital_social

    def extraer_direccion(self, entidades):
        for ent in entidades:
            if ent.category == "Address" and ent.confidence_score > 0.50:
                return ent.text
        return ""

    def extraer_nombres(self, entidades):
        for ent in entidades:
            if (
                ent.category == "Person"
                and ent.confidence_score > 0.50
                and ent.text not in Config.NOMBRES_ENCARGADOS_ORG
            ):
                return ent.text
        return ""
