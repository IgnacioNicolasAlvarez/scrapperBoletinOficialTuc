import re
import spacy
import es_core_news_sm


def get_feature_from_tittle(pattern, text):
    x = []
    try:
        x = re.findall(pattern, text)[0]
    except Exception as e:
        print(f'Error: {e}, Pattern: {pattern}, Text: {text}')
    return x


def encontrar_nombres(text):
    nlp = es_core_news_sm.load()
    texto_taggeado = nlp(text)
    lista_entidades = [(i.text, i.label_) for i in texto_taggeado.ents]
    nombres = []
    for entidad, etiqueta in lista_entidades:
        if etiqueta == 'PER':
            nombres.append(entidad)
    return {f'nombre_{nombres.index(nombre)}': nombre for nombre in list(set(nombres))
            if len(nombre.split(' ')) >= 2 and list(nombre)[0].isupper()}
