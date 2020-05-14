from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/products
    path('', views.index, name="products-index"),
    path('sort_by_price', views.sort_all_by_price, name="sort-by-price"),
    path('sort_by_name', views.index, name="sort-by-name"),
    path('games/sort_by_price', views.sort_games_by_price, name="sort-games-by-price"),
    path('consoles/sort_by_price', views.sort_consoles_by_price, name="sort-consoles-by-price"),
    path('games/sort_by_name', views.sort_games_by_name, name="sort-games-by-name"),
    path('consoles/sort_by_name', views.sort_consoles_by_name, name="sort-consoles-by-name"),
    path('consoles', views.get_all_consoles, name="filter-by-console"),
    path('games', views.get_all_games, name="filter-by-game"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('create_product', views.create_product, name="create_product"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),
    path('update_product/<int:id>', views.update_product, name="update_product"),
]