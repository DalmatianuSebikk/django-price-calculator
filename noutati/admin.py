from django.contrib import admin
from .models import Articol
# Register your models here.

class SeeItems(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'description', 'image')
    search_fields = ['title']

admin.site.register(Articol)
