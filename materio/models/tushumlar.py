from django.db import models


class Kassa(models.Model):
    tushumlar = models.BigIntegerField()
    chiqimlar = models.BigIntegerField()
    foyda = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.foyda
        
