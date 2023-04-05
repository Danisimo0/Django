from django.urls import path, re_path
from . import views


app_name = 'app_name_task_list'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name=''),
    path('home/', views.home, name='home'),
    path('sign_in/', views.sing_in, name='sign_in'),
    path('logout/', views.logout_, name='logout'),
    path('sign_up', views.sign_up, name='register'),


    path('task/create/', views.create, name='create'),
    path('task/<int:task_id>/', views.read, name='read'),
    path('task/list/', views.read_list, name='read_list'),
    path('task/<int:task_id>/update/', views.update, name='update'),
    re_path(r'^task/(?P<task_id>\d+)/delete/$', views.delete, name='delete'),

    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/detail/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/create/', views.post_comment_create, name='post_comment_create'),
    path('post/<int:pk>/comment/delete/', views.post_comment_delete, name='post_comment_delete'),
    path('post_create/', views.post_create, name='post_create'),
]