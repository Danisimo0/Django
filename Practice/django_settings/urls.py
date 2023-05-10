"""
URL configuration for django_settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import grappelli
from django_app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from django_app.views import PostList, UserDetail, UserList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    re_path(r'^posts/$', views.post_list, name='post_list'),
    re_path(r'^posts/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^posts/(?P<pk>\d+)/comments/$', views.CommentView.as_view(), name='comment_list'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
# Первый маршрут привязывается к контроллеруфункции post_list для GET-запросов и
# обрабатывает запросы на страницу со списком постов.

# Второй маршрут привязывается к контроллеру функции post_detail для GET-запросов и
# принимает параметр pk, чтобы получить определенный пост.

# Третий маршрут  который привязывается к контроллеру-классу CommentView для GET и POST-запросов.
# Он принимает параметр pk для идентификации соответствующего поста.