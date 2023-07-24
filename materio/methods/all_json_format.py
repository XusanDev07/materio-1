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


def dokon_ombor(request, params, pk):
    pk = Maxsulot.objects.filter(id=params['pk'])
    if pk:
        return {
            "id": pk.id,
            "product_name": pk.product_name,
            "size": pk.size,
            "color": pk.color,
            "joyi": pk.joyi,
            "product_price": pk.product_price,
            "prodect_price_type": pk.product_price_type,
            "entry_price": pk.entry_price,
            "entry_price_type": pk.entry_price_type
        }
    else:
        pass
