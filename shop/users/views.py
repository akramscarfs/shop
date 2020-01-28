from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from main import views as main_views
from main import models as main_models


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'items': len(main_views.basket_list)})


@login_required
def profile(request):

    user_form = UserUpdateForm(instance=request.user)
    invoices = main_models.Invoice.objects.filter(client_email=request.user.email).all()

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if request.user.is_authenticated:
            if user_form.is_valid():
                user_form.instance.user = request.user
                user_form.save()
                messages.success(request, 'Thank you for successfully updating your profile!')
                return redirect('profile')
        else:

            return redirect('login')

    context = {
        'user_form': user_form,
        'items': len(main_views.basket_list),
        'invoices': invoices,
    }

    return render(request, 'users/profile.html', context)
