from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 200)
    categorie = models.CharField(max_length = 100, default='investigatie')
    description = models.CharField(max_length = 100)
    price = models.FloatField()
    explicatie = models.TextField(blank = True, default = 'explicatie')

