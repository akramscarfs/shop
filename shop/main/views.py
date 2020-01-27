from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime
from django.http import HttpResponseNotFound

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

        model = Invoice()
        model.client_name = request.user.first_name
        model.client_address = request.user.address1
        model.client_email = request.user.email
        model.items = convertListToString(basket_list)
        model.date = str(datetime.date.today())
        subtotal = 0.00
        for i in basket_list:
            subtotal += round(float(i[4]), 2)
        model.delivery = request.POST['delivery-fee']
        model.total_price = round(subtotal, 2)
        grand_total = subtotal + float(request.POST['delivery-fee'])
        model.grand_price = round(grand_total, 2)
        model.save()

        return redirect('invoice', pk=model.id)
    return render(request, 'main/payment.html', {'items': len(basket_list)})


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


class InvoiceDetailView(DetailView):
    model = Invoice

    def get_context_data(self, **kwargs):
        context = super(InvoiceDetailView, self).get_context_data(**kwargs)
        context['invoice'] = Invoice.objects.all().get(pk=self.object.pk)
        this_invoice = Invoice.objects.all().get(pk=self.object.pk)
        context['items'] = convertStringToList(this_invoice.items)

        if self.request.user.email != this_invoice.client_email:
            return None

        return context


def convertListToString(list):
    list_str = ""
    for i in list:
        product_name = i[0]
        size = i[1]
        colour = i[2]
        price = i[6]
        quantity = i[3]
        subtotal = "{0:.2f}".format(float(i[4]))
        item_str = (product_name + ", " + size + ", " + colour + ", "
                + price + ", " + quantity + ", " + subtotal)
        list_str += item_str + "/ "
    return list_str


def convertStringToList(list_string):
    my_list = []
    item_string = list_string.split("/ ")
    for i in item_string:
        if i != item_string[-1]:
            item = []
            for x in i.split(", "):
                item.append(x)
            my_list.append(item)

    return my_list


def redirect():

    return redirect('main-home')
