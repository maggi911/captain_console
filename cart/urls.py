from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/products
    path('', views.index, name="cart-index"),
]