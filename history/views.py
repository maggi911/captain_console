from history.models import UserHistory
from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    h = {"history": UserHistory.objects.all().filter(user_id=request.user.id)}
    #products = {"products": Product.objects.all().order_by("id")}
    user_products = [i.product_id for i in h["history"]]
    context = {"products": Product.objects.filter(id__in=user_products)}
    print(context["products"])
    #context = [i for i in products["products"] if i.id in user_products]
    return render(request, "history/search_history.html", context)