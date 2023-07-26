from methodism import custom_response, MESSAGE
from materio.models import Storage, Storage_order, Client, Maxsulot


def direc_inspection(request):
    if request.user.user_type != 1:
        return custom_response(False, message=MESSAGE['PermissionDenied'])
    return custom_response(True)


def magazin_inspection(request):
    if request.user.user_type != 1:
        return custom_response(False, message=MESSAGE['PermissionDenied'])
    return custom_response(True)


def ombor_inspection(request):
    if request.user.user_type != 1:
        return custom_response(False, message=MESSAGE['PermissionDenied'])
    return custom_response(True)


def get_ombor_clent_dokon(request, params):
    if request.user.user_type != 1:
        return custom_response(False, message=MESSAGE['PermissionDenied'])

    result = {
        "ombor": [x.storage_order_format() for x in Storage_order.objects.all()],
        "mag": [x.clent_format() for x in Client.objects.all()]
    }
    return {
        "result": result
    }
