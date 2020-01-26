from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

basket_list = []
this_invoice_id = 0


class ProductDetailView(DetailView):
    model = Product
    print("works1")
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        form = Item()
        products = Product.objects.all()
        context['products'] = products
        context['form'] = form
        context['items'] = len(basket_list)
        print("works2")

        return context

    def post(self, request, *args, **kwargs):

        form = Item(request.POST)
        print(form)

        if form.is_valid():

            product_form = [form.cleaned_data['product_name'],
                            form.cleaned_data['size'],
                            form.cleaned_data['colour'],
                            form.cleaned_data['quantity'],
                            form.cleaned_data['price'],
                            form.cleaned_data['product_image'],
                            form.cleaned_data['initial_price'],
                            form.cleaned_data['stock']]
            item_in_basket = False
            for i in basket_list:
                if i[0] == product_form[0]:
                    if i[1] == product_form[1]:
                        if i[2] == product_form[2]:
                            i[3] = int(product_form[3]) + int(i[3])
                            if int(product_form[7]) < i[3]:
                                i[3] = product_form[7]
                            i[4] = int(i[3]) * float(i[6])
                            item_in_basket = True

            if item_in_basket is False:
                basket_list.append(product_form)

        return redirect('cart-shop')


def nr_items(request):

    return render(request, 'main/base.html', {'items': len(basket_list)})

def cart(request):
    data = {'product_name': 'product name',
            'size': 'dfk',
            'colour': 'dkvs',
            'quantity': '2',
            'remove': 'no'}

    if request.method == 'POST':
        form = ChangeOrRemove(request.POST)
        if form.is_valid():
            item = [form.cleaned_data['product_name'],
                    form.cleaned_data['size'],
                    form.cleaned_data['colour'],
                    form.cleaned_data['quantity'],
                    form.cleaned_data['remove']]
            a = 0
            for i in basket_list:
                if i[0] == item[0]:
                    if i[1] == item[1]:
                        if i[2] == item[2]:
                            if item[4] == "no":
                                i[3] = item[3]
                                i[4] = float(i[3]) * float(i[6])
                            else:
                                basket_list.pop(a)
                a += 1

    return render(request, 'main/cart.html', {'cart': basket_list, 'form': ChangeOrRemove(data), 'items': len(basket_list)})

@login_required
def payment(request):
    if request.method == 'POST':

        new_list = models.items

        model = Invoice()
        model.client_name = ""
        model.client_address = ""
        model.client_email = ""
        new_list = new_list.append(basket_list)
        model.date = ""
        model.delivery = ""
        model.total_price = ""
        model.grand_price = ""
        model.save()
        print(getattr(Invoice.objects.all().get(id=model.id), 'items'))

        return redirect('this-invoice', pk=model.id)
    return render(request, 'main/payment.html', {'cart': basket_list, 'items': len(basket_list)})


def home(request):
    return render(request, 'main/home.html', {'items': len(basket_list)})


def contact(request):
    return render(request, 'main/contact.html', {'items': len(basket_list)})


def shop(request):
    products = Product.objects.all()

    context = {
        'products': products,
        'items': len(basket_list),
    }

    return render(request, 'main/shop.html', context)


def faq(request):
    return render(request, 'main/faq.html', {'items': len(basket_list)})
