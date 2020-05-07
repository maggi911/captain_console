from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "cart/index.html")

def payment_method(request):
    return render(request, "cart/payment_method.html")

def payment_info(request):
    return render(request, "cart/payment_info.html")

def payment_review(request):
    return render(request, "cart/payment_review.html")

def payment_successful(request):
    return render(request, "cart/payment_successful.html")