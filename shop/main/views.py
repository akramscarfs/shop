from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'main/home.html')


def contact(request):
    return render(request, 'main/contact.html')


def shop(request):
    products = Product.objects.all()


    context = {
        'products': products,
    }

    return render(request, 'main/shop.html', context)

