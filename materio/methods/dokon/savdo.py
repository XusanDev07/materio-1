from materio.models import Maxsulot, Storage_order
from materio.models.savdo import savdo_oynasi as Savdo
from materio.models import Client
from materio.methods.direktor.home_page import magazin_inspection
from methodism import custom_response


def savdo_ooynasi(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.savdo_format() for x in Savdo.objects.all()]
    }


def add_savdo(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result
    Client.objects.filter(phone=request.user.phone).first()

    product = Maxsulot.objects.get(product_name=params['product_name'])
    clent = Client.objects.filter(name=params['clent_name']).first()
    sotish_narx = params['sotish_narxi']
    valyuta = params['valyuta']

    Savdo.objects.get_or_create(product=product, clent_bolsa=clent, sotish_narxi=sotish_narx, valyuta=valyuta)
    return custom_response(status=True, message={"Qilgan savdoyingiz uchun raxmat"})
