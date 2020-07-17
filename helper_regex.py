import re
# ['29774               / 15/07/2020Nro:               77912DECRETO 989 / 2020 DECRETO / 2020-06-18']


def get_head_attr(pattern, text):
    i = 0
    data = []
    for match in re.finditer(pattern, text):
        data.append(match.groups()[i])
        i += 1

    return data
