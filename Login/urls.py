from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Importo la vista creada en views de login inicio
from Login.views import CustomAuthToken
# Importo la vista creada en views de login fin

urlpatterns = [
    re_path(r'^',CustomAuthToken.as_view())
]