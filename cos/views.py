from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import Product
from django import template
# Create your views here.

register = template.Library()

def home(request):
    products = Product.objects.all()
    return render(request, 'cos/home.html', {'products': products})


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
