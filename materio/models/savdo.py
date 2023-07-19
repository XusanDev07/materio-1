from django.db import models

from materio.models import Maxsulot, User
from materio.models.clent import Client

 
class savdo_oynasi(models.Model):

    product = models.ForeignKey(Maxsulot, on_delete=models.SET_NULL, null=True, blank=True)
    clent_bolsa = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)

    sotish_narxi = models.CharField(max_length=50)
    valyuta = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])

    def savdo_format(self):
     return {
      "id": self.id,
      "product_name": self.product.product_name,
      "clent_bolsa": self.clent_bolsa,
      "sotish_narxi": self.sotish_narxi,
      "valyuta": self.valyuta
     }
    def __str__(self):
        return self.product
