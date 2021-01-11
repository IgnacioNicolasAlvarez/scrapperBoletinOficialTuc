from datetime import date, datetime


def obtener_fecha_format():
    today = date.today()
    return today.strftime("%d/%m/%Y")


def obtener_fecha_format(date):
    try:
        day = datetime.strptime(date, "%d/%m/%Y")
        return day.date().strftime("%Y-%m-%d")
    except Exception as e:
        return date
