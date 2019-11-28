from django.shortcuts import render
from django.views.generic import DetailView
from .models import *


def home(request):
    return render(request, 'main/home.html')

class ProductDetailView(DetailView):
    model = Product

def contact(request):
    return render(request, 'main/contact.html')


def shop(request):
    products = Product.objects.all()


    context = {
        'products': products,
    }

    return render(request, 'main/shop.html', context)

