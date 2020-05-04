from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/products
    path('', views.index, name="products-index"),
    path('<int:id>', views.get_product_by_id, name="product_details")
]