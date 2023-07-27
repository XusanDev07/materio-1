from materio.models import Kassa, savdo_oynasi, chetdan_buyurtma
from methodism import custom_response
from django.db.models import Sum


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
    tushumlar_sum = tushumlar_objects.aggregate(Sum('sotish_narxi'))

    chiqimlar_objects = chetdan_buyurtma.objects.all()
    chiqimlar_sum = chiqimlar_objects.aggregate(Sum('narxi'))

    return custom_response(status=True, message={
        "result": tushumlar_sum, chiqimlar_sum
    })
