from django.urls import path
from . import views
from .views import product_list, product_create

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product_create/', views.product_create, name='product_create')
]