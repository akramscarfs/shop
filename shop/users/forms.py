from django import forms
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name', 'country', 'address1', 'address2', 'postcode', 'phone_number', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['country', 'address1', 'address2', 'postcode', 'phone_number']

