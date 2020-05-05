from django.db import models
from products.models import Product, ProductImage

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    product_image = models.ForeignKey(ProductImage, on_delete=models.DO_NOTHING)