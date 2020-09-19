from datetime import date, datetime


def get_current_format_date():
    today = date.today()
    return today.strftime("%d/%m/%Y")


def get_date_in_format(date):
    try:
        day = datetime.strptime(date, '%d/%m/%Y')
        return day.date().strftime('%Y-%m-%d')
    except:
        return date
