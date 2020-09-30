import re


def get_feature_from_tittle(pattern, text):
    x = []
    try:
        x = re.findall(pattern, text)[0]
    except Exception as e:
        print(f'Error: {e}, Pattern: {pattern}, Text: {text}')
    return x