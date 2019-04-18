from django.shortcuts import render
from shop.models import Product


def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "shop/product/list.html", {"products": products})