from materio.methods.direktor.home_page import direc_inspection
from materio.models import Maxsulot, shop, savdo_oynasi
from methodism import custom_response, MESSAGE, error_params_unfilled


def get_dokon(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.dokon_format() for x in shop.objects.all()]
    }


def add_dokon(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    all_info = next((field for field in [
        "name", "location", "product", "employee_number", "savdo",
        "product_number"
    ] if field not in params), '')

    if all_info:
        return custom_response(status=False, message=error_params_unfilled(all_info))

    product = Maxsulot.objects.get(product_name=params['product'])
    savdo = savdo_oynasi.objects.get(id=params['savdo_id'])
    shop.objects.get_or_create(
        name=params['name'],
        location=params['location'],
        employee_number=params['employee_number'],
        product=paramsproduct,
        savdo=savdo,
        product_number=params['product_number']
    )
    return custom_response(status=True, message={"Do'kon qo'shildi"})


def update_dokon(request, params):
    error = next((field for field in [
        "name", "location", "product", "employee_number", "soni", "savdo",
        "product_number"
    ] if field not in params), '')
    if error:
        return custom_response(status=False, message=error_params_unfilled(error))

    try:
        dokon = shop.objects.get(product_number=params['product_number'])
    except shop.DoesNotExist:
        return custom_response(status=False, message=MESSAGE['UserNotFound'])

    dokon.name = params.get('name', dokon.name)
    dokon.location = params.get('location', dokon.location)
    dokon.employee_number = params.get('employee_number', dokon.employee_number)
    dokon.product = params.get('product', dokon.product)
    dokon.savdo = params.get('savdo', dokon.savdo)
    dokon.product_number = params.get('product_number', dokon.product_number)
    dokon.save()
    return custom_response(True, message={"Succes": "Malumot qayta yuklandi"})


def delete_dokon(request, params):
    try:
        ombor = shop.objects.get(id=params['id'])
        ombor.delete()
        return custom_response(status=True, message="Succes")
    except Maxsulot.DoesNotExist:
        return custom_response(status=False, message={"Error": "Bunday dokon topilmadi"})

