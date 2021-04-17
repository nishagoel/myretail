from django.db import models

# Create your models here.


class Product(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    currency_code = models.CharField(max_length=3)
