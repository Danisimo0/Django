from django.urls import path
from myapp.views import my_view

urlpatterns = [
    path('my-view/', my_view, name='my_view'),

]
