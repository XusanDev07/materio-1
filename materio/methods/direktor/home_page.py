from methodism import custom_response, MESSAGE


def direc_inspection(request):
    if request.user.user_type != 1:
        return custom_response(False, message=MESSAGE['PermissionDenied'])
    return custom_response(True)


def magazin_inspection(request):
    if request.user.user_type != 3:
        return custom_response(False, message=MESSAGE['PermissionDenied'])
    return custom_response(True)


def ombor_inspection(request):
    if request.user.user_type != [1, 3]:
        return custom_response(False, message=MESSAGE['PermissionDenied'])
    return custom_response(True)
