from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from cart.models import Cart
from history.models import UserHistory
from products.forms.product_form import ProductCreateForm, ProductUpdateForm
from products.models import Product, ProductImage


# Create your views here.
def index(request):
    if "search_filter" in request.GET:
        search_filter = request.GET["search_filter"]
        products = [ {
            "id": x.id,
            "name": x.name,
            "description": x.description,
            "image": x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({"data": products})
    context = {"products": Product.objects.all().order_by("name")}
    return render(request, "products/index.html", context)

def sort_all_by_price(request):
    if "search_filter" in request.GET:
        search_filter = request.GET["search_filter"]
        products = [ {
            "id": x.id,
            "name": x.name,
            "description": x.description,
            "image": x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({"data": products})
    context = {"products": Product.objects.all().order_by("price")}
    return render(request, "products/index.html", context)

def sort_consoles_by_name(request):
    context = {"products": Product.objects.filter(category=1).order_by("name")}
    return render(request, "products/index.html", context)

def sort_games_by_name(request):
    context = {"products": Product.objects.filter(category=2).order_by("name")}
    return render(request, "products/index.html", context)

def sort_consoles_by_price(request):
    context = {"products": Product.objects.filter(category=1).order_by("price")}
    return render(request, "products/index.html", context)

def sort_games_by_price(request):
    context = {"products": Product.objects.filter(category=2).order_by("price")}
    return render(request, "products/index.html", context)

def get_all_consoles(request):
    context = {"products": Product.objects.filter(category=1).order_by("name")}
    return render(request, "products/index.html", context)

def get_all_games(request):
    context = {"products": Product.objects.filter(category=2).order_by("name")}
    return render(request, "products/index.html", context)

# /products/id
def get_product_by_id(request, id):
    if request.user.id:
        user = get_object_or_404(User, pk=request.user.id)
        product = get_object_or_404(Product, pk=id)
        h = {"history": UserHistory.objects.all().filter(user_id=request.user.id)}
        l = [i.product_id for i in h["history"]]
        if id not in l:
            user_history = UserHistory(user=user, product=product)
            user_history.save()

    return render(request, "products/product_details.html", {
        "product": get_object_or_404(Product, pk=id)
    })

def create_product(request):
    if request.method == "POST":
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST["image"], product=product)
            product_image.save()
            return redirect("products-index")
    else:
        form = ProductCreateForm()
    return render(request, "products/create_product.html", {
        "form": form
    })

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect("products-index")

def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("product_details", id=id)
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, "products/update_product.html", {
        "form": form,
        "id": id
    })