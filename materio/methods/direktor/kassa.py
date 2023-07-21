from materio.models import Kassa, savdo_oynasi, chetdan_buyurtma
from methodism import custom_response

def kassa(request, params):
    try:
        tushumlar = int(params['sotish_narxi'])
        chiqimlar = int(params['chiqimlar_narxi'])
    except ValueError:
        return custom_response(status=False, message={"error": "Sotish narxi va chiqimlar narxi raqam bo'lishi kerak"})

    foyda = tushumlar - chiqimlar
    Kassa.objects.create(tushumlar=tushumlar, chiqimlar=chiqimlar, foyda=foyda)

    return custom_response(status=True, message={"Malumot saqlandi"})

def tushumlar(request, params):
    tushumlar_objects = savdo_oynasi.objects.all()
    tushumlar_sum = sum(tushumlar.sotish_narxi for tushumlar in tushumlar_objects)

    return custom_response(status=True, message={"Tushumlar": tushumlar_sum})

    
