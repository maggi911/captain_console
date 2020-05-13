from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/history
    path('', views.index, name="history-index")
]