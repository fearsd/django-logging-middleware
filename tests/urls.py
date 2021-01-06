from django.urls import path

from .views import *

urlpatterns = [
    path('get_simple', get_simple)
]