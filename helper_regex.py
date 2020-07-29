import re


def get_head_attr(pattern, text):
    return re.findall(pattern, text)[0]
