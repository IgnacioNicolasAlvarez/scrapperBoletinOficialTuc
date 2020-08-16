from datetime import date


def get_current_format_date():
    today = date.today()
    return today.strftime("%d/%m/%Y")
