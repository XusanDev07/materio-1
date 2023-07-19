from materio.methods.auth import regis, login, StepOne, StepTwo, logout, user_update, user_delete
from materio.methods.ombor import add_savat, del_savat, get_savat, add_ombor, get_ombor, update_ombor, \
    delete_ombor, omborga_buyurtma, get_storage_order, delete_storge_order
from materio.methods.direktor import add_xodim, get_xodim, update_xodim, add_product, get_product, update_product,\
    delete_product, kassa
from materio.methods.dokon import add_savdo, savdo_ooynasi, get_clent, add_clent, delete_clent, update_clent,\
    get_dokon, add_dokon, delete_dokon, update_dokon


ununsable_variable = dir()


def all_methods(request, params):
    return {
        "result": [x for x in ununsable_variable if "__" not in x and x not in ['auth', 'ombor']]
    }
