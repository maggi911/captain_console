from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/cart
    path('', views.index, name="cart-index"),
    path('payment_method', views.payment_method, name="payment-method"),
    path('payment_contact', views.payment_contact, name="payment-contact"),
    path('payment_info', views.payment_info, name="payment-info"),
    path('payment_review', views.payment_review, name="payment-review"),
    path('payment_successful', views.payment_successful, name="payment-successful")
]