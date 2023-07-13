from methodism import custom_response, MESSAGE
from materio.models import Maxsulot, Storage, User
from materio.models.savdo import savdo_oynasi
from materio.models import Client
from materio.methods.direktor.home_page import magazin_inspection


def savdo_ooynasi(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result

    if not result['status']:
        return result

    return {
        "result": [x.savdo_format() for x in savdo_oynasi.objects.all()]
    }


def add_savdo(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result
    if request.user.username != Client.objects.get(name) or request.user.phone != Client.objects.get(phone):
        return custom_response(status=False, message={"Siz clentlar ro'yxatida yo'qsiz"})
    
    product = Maxsulot.objects.get(product_name=params['product_name'])
    clent = Client.objects.get(name=params['clent_name'])
    sotish_narx = params['sotish_narxi']
    valyuta = params['valyuta']

    savdo_oynasi.objects.get_or_create(product=product, clent_bolsa=clent, sotish_narxi=sotish_narx, valyuta=valyuta)
    return custom_response(status=True, message={"Qilgan savdoyingiz uchun raxmat"}

