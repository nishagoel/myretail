from django.db import models

# Create your models here.


class ProductDetails(models.Model):
    product_name = models.CharField(max_length=256)
    product_id = models.IntegerField(null=True)