from materio.methods.direktor.home_page import magazin_inspection
from materio.models import Client
from methodism import custom_response, error_params_unfilled, MESSAGE


def get_clent(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.clent_format() for x in Client.objects.all()]
    }


def add_clent(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result

    all_info = next((field for field in [
        "name", "phone", "xabar_berish", "oxirgi_product"
    ] if field not in params), '')

    if all_info:
        return custom_response(status=False, message=error_params_unfilled(all_info))

    clent = Client.objects.filter(name=params['name']).first()
    if clent:
        return custom_response(status=False, message={"Bunaqa user mavjud"})
    
    Client.objects.get_or_create(
        name=params['name'],
        phone=params['phone'],
        xabar_berish=params['xabar_berish'],
        oxirgi_product=params['oxirgi_product']
    )
    return custom_response(status=True, message={"clent qo'shildi"})


def update_clent(request, params):
    error = next((field for field in [
                "name", "phone", "xabar_berish", "oxirgi_product"
    ] if field not in params), '')
    if error:
        return custom_response(status=False, message=error_params_unfilled(error))

    try:
        prod = Client.objects.get(name=params['name'])
    except Client.DoesNotExist:
        return custom_response(status=False, message=MESSAGE['UserNotFound'])

    prod.name = params.get('name', prod.name)
    prod.phone = params.get('phone', prod.phone)
    prod.xabar_berish = params.get('xabar_berish', prod.xabar_berish)
    prod.oxirgi_product = params.get('oxirgi_product', prod.oxirgi_product)
    prod.save()
    return custom_response(True, message={"Succes": "Malumot qayta yuklandi"})


def delete_clent(request, params):
    try:
        clent = Client.objects.get(name=params['name'])
        clent.delete()
        return custom_response(status=True, message="Succes")
    except Client.DoesNotExist:
        return custom_response(status=False, message={"Error": "Clent ochirildi"})
