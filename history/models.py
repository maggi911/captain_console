from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)