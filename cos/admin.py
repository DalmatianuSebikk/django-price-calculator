from django.contrib import admin
from .models import Product

class SeeItems(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'categorie', 'price')
    search_fields = ['name']
    list_editable = ['name', 'description', 'categorie', 'price']

admin.site.register(Product, SeeItems)