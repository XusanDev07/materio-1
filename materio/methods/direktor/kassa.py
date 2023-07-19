from materio.models import Kassa, savdo_oynasi, chetdan_buyurtma
from methodism import custom_response

def kassa(request, params):
  tushumlar = savdo_oynasi.objects.get(sotish_narxi=params['sotish_narxi'])
  if not tushumlar:
    return custom_response(stauts=False, message={"error": "Bunday savdo amalga oshirilmagan"})
  chiqimlar = chetdan_buyurtma.objects.get(narxi=params['chiqimlar_narxi'])
  if not chiqimlar:
    return custom_response(status=False, message={"error": "bunday buyurtma kampaniya tomonidan amalga oshirilmagan"})
  foyda = tushumlar - chiqimlar
  Kassa.objects.create(tushumlar=tushumlar, chiqimlar=chiqimlar, foyda=foyda)
  
  return custom_response(status=True, message={"Malumot saqlandi"})
