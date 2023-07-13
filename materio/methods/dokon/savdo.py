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
    clent = Client.objects.get(name=params['clent_name')
    sotish_narx = params['sotish_narxi']
    valyuta = params['valyuta']

    savdo_oynasi.objects.get_or_create(product=product, clent_bolsa=clent, sotish_narxi=sotish_narx, valyuta=valyuta)
    return custom_response(status=True, message={"Qilgan savdoyingiz uchun raxmat"}



# def buyurtma_oynasi(request, params):
#     result = magazin_inspection(request)
#     if not result['status']:
#         return result

#     if request.user.username != Client.objects.get(name) and request.user.phone != Client.objects.get(phone) or request.user.is_anonymous:
#         return custom_response(status=False, message={"Siz clentlar ro'yxatida yo'qsiz"})
    
    
#     if "product_name" not in params or "maxsulot_soni" not in params or "user_name" not in params:
#         return custom_response(False, message="Params toliq emas")

#     ombor = Storage.objects.filter(id=params["ombor_id"]).first()
#     product = Maxsulot.objects.filter(product_name=params["name"]).first()
#     if not product:
#         return custom_response(False, message="Bunday mahsulot topilmadi")
#     if not ombor:
#         return custom_response(False, message={"bunday ID lik ombor yoq"})

#     if ombor.product_num < params["maxsulot_soni"]:
#         return custom_response(False, message="Mahsulot yetarli emas")

#     a = User.objects.get(username=params['user_name'])
#     if not a:
#         return custom_response(status=False, message={"bunday user yo'q"})

#     savdo_oynasi.objects.get_or_create(product=product, clent_bolsa=a, sotish_narxi=params['narx'], valyuta=params['valyuta'])

#     return custom_response(status=True, message={"Qilgan savdoyingiz uchun raxmat"}
