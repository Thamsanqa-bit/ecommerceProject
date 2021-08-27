from .forms import ProductForm
from django.utils.text import slugify
from django.shortcuts import render, redirect
from . models import Product

# Create your views here.
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.customer = request.user.customer
            product.slug = slugify(product.title)
            product.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, "products/add_products.html", {'form': form})

def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, "products/update_product.html", context)

