# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpRequest
# from django.urls import reverse
# from django.utils import timezone
# from . import models
#
#
# # Create your views here.
# def sign_up(request):
#     if request.method == "POST":
#         username = request.POST.get("username", "")
#         password = request.POST.get("password", "")
#
#         user = User.objects.create_user(username=username, password=password)
#         login(request, user)
#         return redirect(reverse('app_name_task_list:home', args=()))
#     return render(request, 'pages/register.html', context={})
#
#
# def sing_in(request):
#     if request.method == "POST":
#         username = request.POST.get("username", "")
#         password = request.POST.get("password", "")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)  # Сохраняет текушую сессию в cookies browser
#             return redirect(reverse('app_name_task_list:home', args=()))
#         else:
#             raise Exception("Логин или пароль не верны!")
#     return render(request, 'pages/login.html')
#
#
# def logout_(request):
#     logout(request)
#     return redirect(reverse('app_name_task_list:home', args=()))
#
#
# def index(request):
#     return HttpResponse("<h1>This is a Index Page</h1>")
#
#
# def home(request):
#     context = {
#     }
#     return render(request, 'pages/home.html', context)
#
#
# def create(request):
#     if request.method == 'POST':
#         title = request.POST.get("title", "")
#         description = request.POST.get("description", "")
#         models.Task.objects.create(
#             author=User.objects.get(id=1),  
#             title=title,
#             description=description,
#             is_completed=False,
#         )
#         return redirect(reverse('app_name_task_list:read_list', args=()))
#     context = {
#     }
#     return render(request, 'app_task_list/pages/task_create.html', context)
#
#
# def read(request, task_id=None):
#     task = models.Task.objects.get(id=task_id)
#     context = {
#         "task": task
#     }
#     return render(request, 'app_task_list/pages/task_detail.html', context)
#
#
# def read_list(request):
#     is_detail_view = request.GET.get("is_detail_view", True)
#     if is_detail_view == "False":
#         is_detail_view = False
#     elif is_detail_view == "True":
#         is_detail_view = True
#     task_list = models.Task.objects.all()
#
#     def paginate(objects, num_page):
#         paginator = Paginator(objects, num_page)
#         pages = request.GET.get('page')
#         try:
#             local_page = paginator.page(pages)
#         except PageNotAnInteger:
#             local_page = paginator.page(1)
#         except EmptyPage:
#             local_page = paginator.page(paginator.num_pages)
#         return local_page
#
#     page = paginate(objects=task_list, num_page=4)
#     context = {
#         "page": page,
#         "is_detail_view": is_detail_view
#     }
#     return render(request, 'app_task_list/pages/task_list.html', context)
#
#
# def update(request, task_id=None):
#     if request.method == 'POST':
#         task = models.Task.objects.get(id=task_id)
#         is_completed = request.POST.get("is_completed", "")
#         title = request.POST.get("title", "")
#         description = request.POST.get("description", "")
#         if is_completed:
#             if is_completed == "False":
#                 task.is_completed = False
#             elif is_completed == "True":
#                 task.is_completed = True
#         if title and title != task.title:
#             task.title = title
#         if description and description != task.description:
#             task.description = description
#         task.updated = timezone.now()
#         task.save()
#         return redirect(reverse('app_name_task_list:read_list', args=()))
#     task = models.Task.objects.get(id=task_id)
#     context = {
#         "task": task
#     }
#     return render(request, 'app_task_list/pages/task_change.html', context)
#
#
# def delete(request, task_id=None):
#     models.Task.objects.get(id=task_id).delete()
#     return redirect(reverse('app_name_task_list:read_list', args=()))
#
#
# def post_list(request: HttpRequest) -> HttpResponse:
#     posts = models.Post.objects.all()
#     context = {"posts": posts}
#     return render(request, 'app_task_list/pages/post_list.html', context=context)
#
#
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = models.Post.objects.get(id=pk)
#     context = {"post": post}
#     return render(request, 'app_task_list/pages/post_detail.html', context=context)
#
#
# def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
#     post = models.Post.objects.get(id=pk)
#     post.delete()
#     return redirect(reverse('app_name_task_list:post_list', args=()))
#
#
# def post_pk_view(request: HttpRequest, pk: int) -> HttpResponse:
#     if request.method == "GET":
#         context = {}
#         return render(request, 'app_task_list/pages/post_detail.html', context=context)
#     context = {}
#     return render(request, 'app_task_list/pages/post_list.html', context=context)
#
#
# def post_comment_create(request: HttpRequest, pk: int) -> HttpResponse:
#     if request.method == "POST":
#         text = request.POST.get('text', None)
#         post = models.Post.objects.get(id=pk)
#         models.PostComment.objects.create(
#             user=request.user,
#             article=post,
#             text=text,
#         )
#         return redirect(reverse('app_name_task_list:post_detail', args=(pk,)))
#
#
# def post_comment_delete(request: HttpRequest, pk: int) -> HttpResponse:
#     comment = models.PostComment.objects.get(id=pk)
#     pk = comment.article.id
#     comment.delete()
#     return redirect(reverse('app_name_task_list:post_detail', args=(pk,)))
#
#
# def post_create(request: HttpRequest) -> HttpResponse:
#     if request.method == "GET":
#         context = {}
#         return render(request, 'app_task_list/pages/post_create.html', context=context)
#     elif request.method == "POST":
#         print("request: ", request)
#         print("request.POST: ", request.POST)
#         print("request.GET: ", request.GET)
#         print("request.META: ", request.META)
#
#         title = request.POST.get('title', None)
#         description = request.POST.get('description', "")
#         post = models.Post.objects.create(
#             title=title,
#             description=description,
#         )
#         return redirect(reverse('app_name_task_list:post_list', args=()))
#
#
# """ algoritms """
#
#
# # 1)
#
# def is_palindrome_recursive(s):
#
#     if len(s) < 2:
#         return True
#
#
#     if s[0] == s[-1]:
#
#         return is_palindrome_recursive(s[1:-1])
#     else:
#         return False
#
#
# # 2)
#
#
# def is_palindrome_reverse(s):
#
#     s = ''.join(filter(str.isalnum, s)).lower()
#
#     # Сравниваем исходную строку с ее обратным порядком
#     return s == s[::-1]
#
# # 3)
# #
# def is_palindrome_pointers(s):
#
#     s = ''.join(filter(str.isalnum, s)).lower()
#
#     # Используем два указателя: один идет с начала строки, другой с конца
#     left = 0
#     right = len(s) - 1
#
#     while left < right:
#         # Если символы не совпадают, строка не является палиндромом
#         if s[left] != s[right]:
#             return False
#
#         # Перемещаем указатели к центру строки
#         left += 1
#         right -= 1
#
#     return True
#
# # Вроде все 3 решения алгоритма имеют ограничение по памяти О(1)
# # , так как не используют дополнительную память, кроме нескольких переменных, ну если я правильно понял )
#
#
# # 11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
#
#
def compress(numbers):

    numbers.sort()


    start = end = numbers[0]
    result = []


    for i in range(1, len(numbers)):
        if numbers[i] == end + 1:
            end = numbers[i]
        else:

            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")


            start = end = numbers[i]


    if start == end:

        result.append(str(start))
    else:
        result.append(f"{start}-{end}")

    return ','.join(result)


numbers = [1, 2, 3, 4, 7, 8, 10, 11]
result = compress(numbers)
print(result)  # 1-4,7-8,10-11


