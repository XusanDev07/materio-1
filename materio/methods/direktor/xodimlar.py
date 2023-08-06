from methodism import custom_response, MESSAGE, error_params_unfilled
from .home_page import direc_inspection
from materio.models.xodim import Employee


def add_xodim(request, params):
    error = next((field for field in ["name", "phone", "passport"] if field not in params), '')
    if error:
        return custom_response(status=False, message=error_params_unfilled(error))

    try:
        xodim = Employee.objects.filter(passport=params['passport']).first()
        if xodim:
            return custom_response(status=False, message={"error": "bunaqa user bor"})
    except Employee.DoesNotExist:
        return custom_response(status=False, message={"error"})

    saves = Employee.objects.get_or_create(name=params['name'], phone=params['phone'], passport=params['passport'])

    if saves:
        return {
            "urra": "xodim qo'shildi"
        }


def get_xodim(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.employee_format() for x in Employee.objects.all()]
    }


def update_xodim(request, params):
    error = next((field for field in ["name", "phone", "passport"] if field not in params), '')
    if error:
        return custom_response(status=False, message=error_params_unfilled(error))

    try:
        xodim = Employee.objects.get(passport=params['passport'])
    except Employee.DoesNotExist:
        return custom_response(status=False, message=MESSAGE['UserNotFound'])

    xodim.name = params.get('name', xodim.name)
    xodim.phone = params.get('phone', xodim.phone)
    xodim.passport = params.get('passport', xodim.passport)
    xodim.save()
    return custom_response(True, message={"Succes"})



def delete_xodim(request, params):
    
    ombor = Employee.objects.get(id=params['pk'])
    ombor.delete()
    return custom_response(status=True, message="Succes")
    
