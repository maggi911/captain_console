from history.models import UserHistory
from django.shortcuts import render
from products.models import Product

# Create your views here.

# get all products in current user search history
def index(request):
    h = {"history": UserHistory.objects.all().filter(user_id=request.user.id)}
    user_products = [i.product_id for i in h["history"]]
    context = {"products": Product.objects.filter(id__in=user_products)}
    return render(request, "history/search_history.html", context)