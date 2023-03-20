from django.urls import path
from .views import RegIn

urlpatterns = [
    path("regin/", RegIn),
]