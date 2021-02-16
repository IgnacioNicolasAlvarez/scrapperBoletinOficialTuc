from datetime import date, datetime


def obtener_fecha_format(fecha = None):
    hoy = date.today()
    if fecha:
        try:
            if isinstance(fecha, str):
                return fecha
            return fecha.strftime("%d/%m/%Y")
        except Exception as e:
            print(e)
            return hoy.strftime("%d/%m/%Y")

    return hoy.strftime("%d/%m/%Y")
