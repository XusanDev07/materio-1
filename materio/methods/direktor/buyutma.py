from methodism import custom_response

from materio.methods.direktor.home_page import direc_inspection
from materio.models import chetdan_buyurtma


def get_chetdan_buyurtma(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.chetdan_buyurtma_format() for x in chetdan_buyurtma.objects.all()]
    }


def add_chetdan_buyurtma(request, params):
    sh = params['shartnome_raqami']
    d = params['davlat_nomi']
    z = params['zavod_nomi']
    date = params['date']
    h = params['holati']
    m = params['maxsulot'],
    ms = params['maxsulot_soni']
    n = params['narxi']

    if not sh or d or z or date or h or m or ms or n:
        return custom_response(status=False, message={'Error': "malumotlar yetarli emas to'ldir"})

    chetdan_buyurtma.objects.create(sh, d, z, date, h, m, ms, n)
    return custom_response(status=True, message={"Succes": "Chet elga Buyurtma qilindi !"})
