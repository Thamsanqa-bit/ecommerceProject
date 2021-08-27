from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import *
from products.models import Product

#Create your views here.
def home(request):
    return render(request, "accounts/home.html")


def become_customer(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
           user = form.save()
           login(request, user)
           customer = Customer.objects.create(name=user.username, created_by=user)
           return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, "accounts/register.html", context)

def customer(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "accounts/customer.html", context)

# @login_required
# def customer_admin(request):
#     customer = request.user.customer
#     context = {
#         'customer': customer
#     }
#     return render(request, "accounts/customer_admin.html", context)
