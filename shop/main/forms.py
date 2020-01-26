from django import forms


class Item(forms.Form):
    product_name = forms.CharField(max_length=100)
    size = forms.CharField(max_length=100)
    colour = forms.CharField(max_length=100)
    quantity = forms.CharField(max_length=100)
    price = forms.CharField(max_length=100)
    product_image = forms.CharField()
    initial_price = forms.CharField(max_length=100)
    stock = forms.CharField(max_length=100)


class ChangeOrRemove(forms.Form):
    product_name = forms.CharField(max_length=100)
    size = forms.CharField(max_length=100)
    colour = forms.CharField(max_length=100)
    quantity = forms.CharField(max_length=100)
    remove = forms.CharField(max_length=100)

