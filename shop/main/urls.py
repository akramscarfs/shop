from django.urls import path
from . import views
from .views import ProductDetailView, InvoiceDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='main-home'),
    path('contact/', views.contact, name='main-contact'),
    path('shop/', views.shop, name='main-shop'),
    path('shop/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('faq/', views.faq, name='faq'),
    path('cart/', views.cart, name='cart-shop'),
    path('payment/', views.payment, name='payment'),
    path('invoice/<int:pk>/', login_required(InvoiceDetailView.as_view()), name='invoice'),
]
