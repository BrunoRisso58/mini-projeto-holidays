from django.http import HttpResponse
from datetime import date

def isHoliday(today = date.today()):
    if isinstance(today, date):
        today = str(today)
    today = today[5:]
    holiday = "um dia comum ou outro feriado"
    if today == "12-25":
        holiday = "Natal"
    elif today == "04-21":
        holiday = "Tiradentes"
    return holiday

isHoliday()

def index(request):
    holiday = isHoliday()
    return HttpResponse("É " + holiday)
