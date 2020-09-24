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
from django.urls import path, include
from django.conf.urls.static import static
from cos import views
import noutati

from . import settings

urlpatterns = [
    path('', views.home, name = 'Home'),
    path('analize/', views.analize, name = 'analize'),
    path('consultatii-si-echografii/', views.consultatii, name = 'consultatii'),
    path('avize/', views.avize, name = 'avize'),
    path('admin/', admin.site.urls),

    #PENTRU FILTRE
    path('analize/filtru/', views.filtru, name = 'filtru'),
    path('search/', views.search, name = 'search'),
    path('explicatie/<int:analiza_id>/', views.explicatie, name = 'explicatie'),

    #PENTRU CUMPARATURI
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail,name='cart_detail'),

    #PENTRU TRIMIS MAIL 
    path('email/', views.formEmail, name = 'formEmail'),
    path('sendemail/', views.sendEmail, name = 'sendEmail'),

    #PENTRU NOUTATI
    path('noutati/', include('noutati.urls'), name = "vezi_noutati"),
    
] + static(settings.STATIC_URL) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)