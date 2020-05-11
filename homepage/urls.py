from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.index, name="homepage-index"),
    path('aboutus', views.aboutus, name="homepage-aboutus"),
    path('contactus', views.contactus, name="homepage-contactus"),
]