from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.index, name="homepage-index"),
]