import json
import requests

# token = "token eskizdan olinadi !!!"


def send_sms(otp, phone):
    url = "https://notify.eskiz.uz/api/message/sms/send"
    msg = f"Maxfiy kod {otp}"

    data = json.dumps({
        "phone_number": str(phone),
        "message": msg,
        "from": 4546,
        "callback_url": "http://0000.uz/test.php"
    })

    headers = f"Bearer {token}"
    response = requests.post(url, data=data, headers=headers)
    return response
