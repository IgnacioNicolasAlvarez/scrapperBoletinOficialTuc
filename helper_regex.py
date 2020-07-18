import re


def get_head_attr(pattern, text):
    i = 0
    data = []
    for match in re.finditer(pattern, text):
        data.append(match.groups()[i])
        i += 1

    return data
