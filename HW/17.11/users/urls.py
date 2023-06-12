from django.urls import path
from .views import user_list

app_name = 'users'

urlpatterns = [
    path('list/', user_list, name='user_list'),
]
