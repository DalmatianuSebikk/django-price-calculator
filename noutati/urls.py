from django.urls import path
from . import views
urlpatterns = [
    path('', views.vezinoutati, name="Noutati")
]