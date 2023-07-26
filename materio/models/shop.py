from django.db import models
from materio.models import Maxsulot
from materio.models import savdo_oynasi as Savdo


class shop(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    employee_number = models.IntegerField(default=1)
    product = models.ForeignKey(Maxsulot, on_delete=models.SET_NULL, null=True, blank=True)
    savdo = models.ForeignKey(Savdo, on_delete=models.SET_NULL,  null=True)
    product_number = models.IntegerField()
    color = models.CharField(max_length=128)

    def dokon_format(self):
        return {
            'id': self.id,
            "name": self.name,
            'location': self.location,
            'employee_number': self.employee_number,
            'product': self.product.product_name,
            'savdo': self.savdo.sotish_narxi,
            'product_number': self.product_number,
            'valyuta': self.product.product_price_type,
            'color': self.color

        }

    
    def __str__(self):
        return self.name
