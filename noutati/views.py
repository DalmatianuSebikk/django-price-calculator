from django.shortcuts import render
from django import template
from .models import Articol
# Create your views here.


def vezinoutati(req):
    articole = Articol.objects.all()
    return render(req, 'noutati/rendernoutati.html', {'articole': articole})