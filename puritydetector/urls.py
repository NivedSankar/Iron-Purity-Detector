from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
urlpatterns = [
                path('api/', include(router.urls)),
                path('', views.FormView, name='form'),
              ]