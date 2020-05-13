from django.contrib.auth.models import User
from products.models import Product
from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_image = models.CharField(max_length=9999)
    # profile_image = models.ImageField(upload_to="profile_image")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'