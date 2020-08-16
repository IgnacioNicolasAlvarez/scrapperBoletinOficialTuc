from datetime import date, datetime


def get_current_format_date():
    today = date.today()
    return today.strftime("%d/%m/%Y")


def get_date_in_format(date_time_str):
    day = datetime.strptime(date_time_str, '%d/%m/%Y')
    return day.date().strftime('%Y-%m-%d')
