from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('contact/', views.contact, name='main-contact'),
    path('shop/', views.shop, name='main-shop'),
]
