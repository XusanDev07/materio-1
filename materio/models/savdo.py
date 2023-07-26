from django.db import models

from materio.models import Maxsulot, shop
from materio.models.clent import Client


class savdo_oynasi(models.Model):
    product = models.ForeignKey(Maxsulot, on_delete=models.SET_NULL, null=True, blank=True)
    clent_bolsa = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)

    sotish_narxi = models.IntegerField(default=0)
    valyuta = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])
    dokon = models.ForeignKey(shop, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def savdo_format(self):
        return {
            'id': self.id,
            'product': self.product.product_name,
            'sotish_narxi': self.sotish_narxi,
            'valyuta': self.valyuta,
            "dokon": self.dokon.name,
            "date": self.date
        }
