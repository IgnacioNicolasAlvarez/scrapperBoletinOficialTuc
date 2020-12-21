import re

from logger import guardar_log


def get_feature_from_tittle(pattern, text):
    x = []
    try:
        x = re.findall(pattern, text)[0]
    except Exception as e:
        guardar_log(
                "error", f"Imposibilidad de aplicar patron - Pattern: {pattern}"
            )
    return x
