from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import Product
from django import template
# Create your views here.

register = template.Library()

def home(req):
    products = Product.objects.all()
    return render(req, 'cos/home.html', {'products': products})

def analize(request):
    products = Product.objects.filter(categorie='analiza')
    return render(request, 'cos/analize.html', {'products': products})

def consultatii(request):
    products = Product.objects.all()
    return render(request, 'cos/consultatii.html', {'products': products})

def avize(request):
    products = Product.objects.filter(categorie='aviz')
    return render(request, 'cos/avize.html', {'products': products})


def search(req):
    searchItem = req.GET.get('search')
    products = Product.objects.all()
    return render(req, 'cos/search.html', {'searchItem': searchItem, 'products': products})

def filtru(req):
    categorie = req.GET.get('categorie')
    products = Product.objects.filter(description=categorie)
    return render(req, 'cos/filtru.html', {'products': products, 'categorie': categorie})

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product = product)
    return redirect("Home")

def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

def cart_detail(request):
    cart_obj = Cart(request)
    total = sum(
    [
        float(item["price"]) 
        for product_id, item in cart_obj.cart.items()
    ]
    )
    return render(request, 'cos/cos.html', {'total': total})
