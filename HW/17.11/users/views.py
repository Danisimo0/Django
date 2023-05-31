from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import User


def user_list(request):
    users = User.objects.all()

    # Пагинация
    paginator = Paginator(users, 10)  # Показывать 10 пользователей на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Поиск
    query = request.GET.get('q')
    if query:
        users = users.filter(Q(name__icontains=query) | Q(email__icontains=query))

    # Фильтрация
    filter_name = request.GET.get('name')
    if filter_name:
        users = users.filter(name=filter_name)

    return render(request, 'users/user_list.html', {'users': page_obj})
