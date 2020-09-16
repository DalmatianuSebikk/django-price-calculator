"""magazin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
import cos
import noutati

from . import settings

urlpatterns = [
    path('', cos.views.home, name = 'Home'),
    path('analize/', cos.views.analize, name = 'analize'),
    path('consultatii-si-echografii/', cos.views.consultatii, name = 'consultatii'),
    path('avize/', cos.views.avize, name = 'avize'),
    path('admin/', admin.site.urls),


    #PENTRU FILTRE
    path('analize/filtru/', cos.views.filtru, name = 'filtru'),
    path('search/', cos.views.search, name = 'search'),

    #PENTRU CUMPARATURI
    path('cart/add/<int:id>/', cos.views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', cos.views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', cos.views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', cos.views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cos.views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',cos.views.cart_detail,name='cart_detail'),


    #PENTRU NOUTATI
    path('noutati/', noutati.views.vezinoutati, name = "vezi_noutati"),
] + static(settings.STATIC_URL)