from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    full_name = forms.CharField(max_length=50, label='Full Name *')
    country = forms.CharField(max_length=30, label='Country *')
    city = forms.CharField(max_length=30, label='City *')
    address1 = forms.CharField(max_length=50, label='Address 1 *')
    address2 = forms.CharField(max_length=50, label='Address 2 (optional)', required=False)
    post_code = forms.CharField(max_length=10, label='Post Code')

    def signup(self, request, user):
        user.full_name = self.cleaned_data['full_name']
        user.country = self.cleaned_data['country']
        user.city = self.cleaned_data['city']
        user.address1 = self.cleaned_data['address1']
        user.address2 = self.cleaned_data['address2']
        user.post_code = self.cleaned_data['post_code']
        user.save()

        return user
