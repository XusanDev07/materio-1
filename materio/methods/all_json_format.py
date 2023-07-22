from materio.models.base import Maxsulot
from materio.models.base import Storage, Storage_order
from materio.models import shop

def maxsulot_format(data: Maxsulot):
    return {
        "id": data.id,
        "product_name": data.product_name,
        "size": data.size,
        "color": data.color,
        "joyi": data.joyi,
        "product_price": data.product_price,
        "prodect_price_type": data.product_price_type,
        "entry_price": data.entry_price,
        "entry_price_type": data.entry_price_type
    }


def dokon_maxsulot(request, data:shop, pk):
    a = Maxsulot.objects.filter(id=pk).first()
    if a:
         return {
            "id": a.id,
            "product_name": a.product_name,
            "size": a.size,
            "color": a.color,
            "joyi": a.joyi,
            "soni": a.soni,
            "product_price": a.product_price,
            "entry_price": a.entry_price,
            "product_price_type": a.product_price_type,
            "entry_price_type": a.entry_price_type
        }
    else:
        return custom_response(status=False, message={"Error": "Id kirib kemadi shunga malumotlani chiqaromimiz"})
    
