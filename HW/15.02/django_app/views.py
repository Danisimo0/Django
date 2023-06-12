from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Product, ProductCategory
from django.db import transaction


@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = {
            'products': list(products.values())
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category_id')
        category = get_object_or_404(ProductCategory, pk=category_id)
        product = Product(name=name, category=category)
        product.save()
        data = {
            'product': {
                'id': product.id,
                'name': product.name,
                'category': product.category.name
            }
        }
        return JsonResponse(data)


@csrf_exempt
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        data = {
            'product': {
                'id': product.id,
                'name': product.name,
                'category': product.category.name
            }
        }
        return JsonResponse(data)
    elif request.method == 'PUT':
        name = request.POST.get('name')
        category_id = request.POST.get('category_id')
        category = get_object_or_404(ProductCategory, pk=category_id)
        product.name = name
        product.category = category
        product.save()
        data = {
            'product': {
                'id': product.id,
                'name': product.name,
                'category': product.category.name
            }
        }
        return JsonResponse(data)
    elif request.method == 'DELETE':
        product.delete()
        data = {
            'message': 'Product deleted successfully'
        }
        return JsonResponse(data)


def product_category_list(request):
    if request.method == 'GET':
        categories = ProductCategory.objects.all()
        data = {
            'categories': list(categories.values())
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        name = request.POST.get('name')
        category = ProductCategory(name=name)
        category.save()
        data = {
            'category': {
                'id': category.id,
                'name': category.name
            }
        }
        return JsonResponse(data)


@transaction.atomic
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_name = request.POST.get('category')
        price = request.POST.get('price')
        category, created = ProductCategory.objects.get_or_create(name=category_name)
        product = Product(name=name, category=category, price=price)
        product.save()
        return redirect('product_list')
    else:
        categories = ProductCategory.objects.all()
        return render(request, 'product_create.html', {'categories': categories})