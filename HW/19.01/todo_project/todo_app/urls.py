from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.get_todos, name='get_todos'),
    path('todos/create/', views.create_todo, name='create_todo'),
    path('todos/toggle/', views.toggle_todo, name='toggle_todo'),
    path('todos/delete/', views.delete_todo, name='delete_todo'),
]
