from methodism import custom_response, error_params_unfilled

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
    all_info = next((field for field in [
        "shartnome_raqami", "davlat_nomi", "zavod_nomi", "date", "holati", "maxsulot", "maxsulot_soni", "narxi"
    ] if field not in params), '')

    if all_info:
        return custom_response(status=False, message=error_params_unfilled(all_info))

    chetdan_buyurtma.objects.get_or_create(
        shartnome_raqami=sh,
        davlat_nomi=d,
        zavod_nomi=z,
        date=date,
        holati=h,
        maxsulot=m,
        maxsulot_soni=ms,
        narxi=n
    )

    return custom_response(status=True, message={"Succes": "Chet elga buyurtma qilindi"})