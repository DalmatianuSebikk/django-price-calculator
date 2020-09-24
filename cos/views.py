from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .models import Product
from django import template
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect


register = template.Library()

# -------------------- AFISAJ PAGINI PRINCIPALE --------------------

def home(req):
    products = Product.objects.all()
    return render(req, 'cos/home.html', {'products': products})

def analize(request):
    products = Product.objects.filter(categorie='analiza')
    return render(request, 'cos/analize.html', {'products': products})


def explicatie(request, analiza_id):
    analiza = get_object_or_404(Product, pk = analiza_id)
    return render(request, 'cos/explicatii.html', {'analiza': analiza})

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

def formEmail(req):
    return render(req, 'cos/formEmail.html')

# -------------EMAIL-------------------

def sendEmail(request):
    cart_obj = Cart(request)
    numeInv = ""

    destinatar = "sebastianionelbeats@gmail.com"
    subiect = "Programare investigatii"
    nume = request.POST.get('nume')
    telefon = request.POST.get('telefon')

    mesaj = "Buna ziua, ma numesc " + nume + " si as dori sa efectuez urmatoarele investigatii: "

    for product_id, item in cart_obj.cart.items():
        numeInv = numeInv + item["name"] + ", "
    
    mesaj = mesaj + " " + numeInv
    mesaj = mesaj[:-2] + ". Numarul meu de telefon este: " + telefon 
    
    if destinatar and subiect and mesaj:
        email = EmailMessage(subiect, mesaj, to=[destinatar])
        email.send()
        return HttpResponse('Succes')
    else:
        return HttpResponse('NU')



# ---------------- COS DE CUMPARATURI ---------------------

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
