import re
from textwrap import wrap

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


MODEL_URL = "mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"


class NLP:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_URL, do_lower_case=False)
        self.model = AutoModelForQuestionAnswering.from_pretrained(MODEL_URL)

    def _extraer_contenido_nlp(self, pregunta, texto):

        nlp = pipeline("question-answering", model=self.model, tokenizer=self.tokenizer)
        salida = nlp({"question": pregunta, "context": texto.replace(".", "").lower()})
        return salida["answer"]

    def extraer_razon_social(self, pregunta, texto):

        respuesta = self._extraer_contenido_nlp(pregunta, texto)
        return respuesta

    def extraer_capital_social(self, pregunta, texto):
        capital_social = 0
        respuesta = self._extraer_contenido_nlp(pregunta, texto)

        pattern = r"\$*(\d+)"
        encontrado = re.search(pattern, respuesta)
        if encontrado:
            y = int(encontrado.group(1))
            capital_social = y if y > 10000 else 0
        return str(capital_social)
