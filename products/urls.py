from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/products
    path('', views.index, name="products-index"),
    path('sort_by_price', views.sort_by_price, name="sort-by-price"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('create_product', views.create_product, name="create_product"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),
    path('update_product/<int:id>', views.update_product, name="update_product"),
]