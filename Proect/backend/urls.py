from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    register_view,
    login_view,
    LogoutView,
    create_checkout_session,
    UserViewSet,
    UserCreateView,
    CurrentUserView,
    user_list,
    user_create,
    user_update,
    user_delete
)

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('current-user/', CurrentUserView.as_view(), name='current_user'),
    path('user-list/', user_list, name='user_list'),
    path('user-create/', user_create, name='user_create'),
    path('user-update/<int:user_id>/', user_update, name='user_update'),
    path('user-delete/<int:user_id>/', user_delete, name='user_delete'),
    path('', include(router.urls)),
]
