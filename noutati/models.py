from django.db import models
import datetime
class Articol(models.Model):
    title = models.CharField (max_length = 200)
    date = models.DateField(default = datetime.date.today)
    description = models.TextField()
    image = models.ImageField(blank = True)
