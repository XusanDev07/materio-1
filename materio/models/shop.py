from django.db import models
from materio.models import savdo_oynasi, Maxsulot


class shop(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    employee_number = models.IntegerField(default=1)
    product = models.ForeignKey(Maxsulot, on_delete=models.SET_NULL, null=True, blank=True)
    savdo = models.ForeignKey(savdo_oynasi, on_delete=models.SET_NULL,  null=True)
    product_number = models.IntegerField()

    def dokon_format(self):
        return {
            'id': self.id,
            "name": self.name,
            "location": self.location,
            "employee_number": self.employee_number,
            "product": self.product.product_name,
            "savdo": self.savdo.product,
            "product_number": self.product_number
        }

    def __str__(self):
        return self.name
