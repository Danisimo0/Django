from django.contrib import admin
from django.urls import path
from todo import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo'
urlpatterns = [
    path('', views.log_auth, name='log_auth'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)