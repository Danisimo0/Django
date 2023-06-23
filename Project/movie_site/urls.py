"""
URL configuration for movie_site project.

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

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
import debug_toolbar
from movies.forms import SetNewPasswordForm, ResetPasswordForm
from movies.views import CustomErrorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('400/', CustomErrorView.as_view(), name='handler400'),
    path('403/', CustomErrorView.as_view(), name='handler403'),
    path('404/', CustomErrorView.as_view(), name='handler404'),
    path('500/', CustomErrorView.as_view(), name='handler500'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('restapi/', include('RestAPI.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('password-reset/', include([
        path('',
             auth_views.PasswordResetView.as_view(
                 template_name='reset_password/password_reset.html', form_class=ResetPasswordForm),
             name='password_reset'),
        path('done/',
             auth_views.PasswordResetDoneView.as_view(template_name='reset_password/password_reset_done.html'),
             name='password_reset_done'),
        path('confirm/<uidb64>/<token>/',
             auth_views.PasswordResetConfirmView.as_view(
                 template_name='reset_password/password_reset_confirm.html', form_class=SetNewPasswordForm),
             name='password_reset_confirm'),
        path('complete/',
             auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/password_reset_complete.html'),
             name='password_reset_complete'),
    ])),
    path("", include("movies.urls")),
]
#
# handler400 = CustomErrorView.as_view()
# handler403 = CustomErrorView.as_view()
# handler404 = CustomErrorView.as_view()
# handler500 = CustomErrorView.as_view()

if settings.DEBUG:
    # Добавление debug_toolbar в urlpatterns только в режиме DEBUG

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    # Добавление обработки статических файлов в режиме DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
