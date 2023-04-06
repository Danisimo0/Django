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
from django.urls import path
from django.urls.conf import include
from django.urls import re_path

from chat import views
from django.contrib import admin

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import routing

application = ProtocolTypeRouter({
    # http protocol router
    'http': URLRouter([
        path('admin/', admin.site.urls),
        path('accounts/', include('django.contrib.auth.urls')),
        path('signup/', views.SignUp.as_view(), name='signup'),
        path('/home/', views.HomePageView.as_view(), name='home'),
        re_path(r'^sw.js$', views.ServiceWorkerView.as_view(), name='sw.js'),
    ]),

    # websocket protocol router
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),

})
