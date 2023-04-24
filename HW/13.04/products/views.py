# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from .models import Product
#
#
# class ProductList(ListView):
#     model = Product
#     template_name = 'products/product_list.html'
#
#
# class ProductDetail(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#
#
# class ProductCreate(CreateView):
#     model = Product
#     fields = ['name', 'description', 'price', 'image']
#     template_name = 'products/product_form.html'
#
#
# class ProductUpdate(UpdateView):
#     model = Product
#     fields = ['name', 'description', 'price', 'image']
#     template_name = 'products/product_form.html'
#
#
# class ProductDelete(DeleteView):
#     model = Product
#     success_url = reverse_lazy('product_list')
#     template_name = 'products/product_confirm_delete.html'


from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
from .forms import ProductForm

class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'image']
    template_name = 'products/product_form.html'


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'image']
    template_name = 'products/product_form.html'


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    template_name = 'products/product_confirm_delete.html'


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/home.html', context)


def about(request):
    return render(request, 'products/about.html')


def contact(request):
    return render(request, 'products/contact.html')


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'products/product_form.html', context)


def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'products/product_form.html', context)


def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    context = {'product': product}
    return render(request, 'products/product_confirm_delete.html', context)
