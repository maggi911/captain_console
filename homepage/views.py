from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "homepage/index.html")

def aboutus(request):
    return render(request, "homepage/aboutus.html")

def contactus(request):
    return render(request, "homepage/contactus.html")