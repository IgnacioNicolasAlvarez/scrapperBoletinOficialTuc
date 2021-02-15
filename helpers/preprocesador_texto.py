import re


def preprocesar(texto):

    tokens = re.compile(r"\s+").split(texto)
    tokens_sin_decimales = list(map(eliminar_decimales, tokens))
    tokens_sin_peso = list(map(eliminar_espacio_signo_peso, tokens_sin_decimales))

    texto = " ".join(tokens_sin_peso)
    return eliminar_espacios(texto)


def eliminar_decimales(texto):
    aux = re.search(r"(?:,|\.)[0-9]{2}(?![0-9]+)", texto)
    if aux:
        texto = "".join(list(texto)[: aux.start()])
    return texto.replace(".", "")


def eliminar_espacio_signo_peso(texto):
    aux = re.search(r"(\$\s[0-9]*)", texto)
    if aux:
        texto_sin_espacio = list(texto[aux.start() : aux.end()])
        texto_sin_espacio[1] = ""
        return "".join(texto_sin_espacio)
    return texto


def eliminar_espacios(texto):
    return " ".join(texto.split())
