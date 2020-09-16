from django.db import models

class Articol(models.Model):
    title = models.CharField (max_length = 200)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(blank = True)
