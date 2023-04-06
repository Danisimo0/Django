from django.urls import path
from django.urls.conf import include
from django.urls import re_path

from . import views
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
