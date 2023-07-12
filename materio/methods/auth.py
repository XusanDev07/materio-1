import datetime, re, random, string, uuid
from methodism import custom_response, error_params_unfilled, MESSAGE, error_msg_unfilled, generate_key, code_decoder
from rest_framework.authtoken.models import Token
from materio.models import User
from base.server import check_email_in_db, check_token_in_db, check_user_in_token_db, update_token
from base.sen_email import send_email
from materio.models.auth import OTP


def regis(requests, params):
    nott = 'token' if 'token' not in params else 'password' if 'password' not in params else ''

    if nott:
        return custom_response(False, message=f"{nott} paramsda bo'lishi kere")

    token = check_token_in_db(params['token'])

    if not token:
        return custom_response(False, message="Token xato")

    if token['is_expire']:
        return custom_response(False, message="Token yaroqsiz!")

    if not token['is_conf']:
        return custom_response(False, message="Token tastiqlanmagan")

    if len(str(params['password'])) < 8 or " " in params['password']:
        return custom_response(False, message="Parol 8tadan kichkina bolishi kerak emas")

    user_data = {
        'phone': params.get('phone', " "),
        'password': params['password'],
        'username': params.get('username', " "),
        'last_name': params.get('last_name', " "),
        'email': token['email']
    }

    if params.get('key', None):
        user_data.update({
            "is_staff": True,
            "is_superuser": True,
            "user_type": params['key']  # 1-derector 2-ombor 3-magazin
        })
    user = User.objects.create_user(**user_data)
    token = Token.objects.create(user=user)
    return custom_response(True, data=token.key)


def login(requests, params):
    nott = 'password' if 'password' not in params else 'email' if 'email' not in params else ''

    if nott:
        return custom_response(False, message=f"{nott} paramsda bo'lishi kerak")

    user = User.objects.filter(email=params['email']).first()
    if not user:
        return custom_response(False, message='Bu nomerga user yo"q')

    # password = params['password']

    if not user.check_password(params['password']):
        return custom_response(False, message='Parol xato')

    token = Token.objects.get_or_create(user=user)[0]

    return custom_response(True, data={"token": token.key}, message="Login bo'ldi")


def logout(requests, params):
    token = Token.objects.filter(user=requests.user).first()

    if token:
        token.delete()

    return custom_response(True, message="Token o'chirildi")


def StepOne(requests, params):
    # send_email()
    if 'email' not in params:
        return custom_response(False, message="Data to'liq emas")

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not re.fullmatch(regex, params['email']):
        return custom_response(False, message="Xato email")

    code = random.randint(1000000, 9999999)

    send_email(OTP=code, email=params['email'])

    shifr = uuid.uuid4().__str__() + '&' + str(code) + '&' + generate_key(21)
    shifr = code_decoder(shifr, l=3)

    otp = OTP.objects.create(key=shifr, email=params['email'])

    return custom_response(True, data={
        'otp': code,
        'token': otp.key
    })


def StepTwo(requests, params):
    nott = 'otp' if 'otp' not in params else 'token' if 'token' not in params else ''
    if nott:
        return custom_response(False, message=f"{nott} paramsda bo'lishi kerak")

    token = check_token_in_db(params['token'])
    if not token:
        return custom_response(False, message="Token xato")

    if token['is_conf']:
        return custom_response(False, message="Token ishlatilgan")

    if token['is_expire']:
        return custom_response(False, message="Token eski")

    now = datetime.datetime.now(datetime.timezone.utc)

    if (now - token['created']).total_seconds() >= 180:
        token['is_expire'] = True
        update_token(token)
        return custom_response(False, message="Tokenga berilgan vaqt tugadi")

    code = code_decoder(token['key'], decode=True, l=3).split('&')[1]

    if str(params['otp']) != code:
        token['tries'] += 1
        update_token(token)

        return custom_response(False, message="Kode xato")

    token['is_conf'] = True
    update_token(token)

    return custom_response(True, message="Ishladi", data={'otp': code})


def user_update(request, params):
    nott = 'password' if 'password' not in params else 'new_password' if 'new_password' not in params else ''
    if nott:
        custom_response(True, error_msg_unfilled(nott))
    if not request.user.check_password(params['password']):
        return custom_response(True, message={"Error": "Parol noto'g'ri"})

    if request.user.check_password(params['new_password']):
        return custom_response(True, message={"Error": "Parol eskisi bilan teng bo'lishi kerek emas"})

    if len(str(params['new_password'])) < 8 or " " in params['new_password']:
        return custom_response(False, message="Parol 8tadan kichkina va bo'shliq bolishi kerak emas")

    request.user.set_password(params['new_password'])
    request.user.save()

    user = User.objects.filter(phone=params['phone']).first()

    if type(params['phone']) is not int and len(str(params['phone'])) < 12:
        error_msg = f"'{params['phone']}' phone 👈 12ta raqam"
        return custom_response(True, message=error_params_unfilled(error_msg))
    if user and user.id != request.user.id:
        return custom_response(True, message={"Error": "Bunaqa user band qilingan"})

    request.user.phone = params.get('phone', request.user.phone)
    request.user.username = params.get('username', request.user.phone)
    # request.user.email = params.get('email', request.user.email)
    request.user.last_name = params.get('last_name', request.user.last_name)
    request.user.save()
    return custom_response(True, message={"Succes": "User update qilindi"})


def user_delete(request, params):
    request.user.delete()
    return custom_response(True, message=MESSAGE['UserSuccessDeleted'])


def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
