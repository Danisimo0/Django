from django.contrib.auth import logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django_app import models
from .forms import ProfileUpdateForm
import psycopg2
import requests
from bs4 import BeautifulSoup


# Create your views here.


class HomeView(View):
    template_name = 'django_app/home.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {}

        # return JsonResponse(data={"response": 'res'}, safe=True)
        return render(request, 'django_app/home.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        context = {}

        # return JsonResponse(data={"response": 'res'}, safe=True)
        return render(request, 'django_app/home.html', context=context)


def home_view(request: HttpRequest) -> HttpResponse:
    context = {}

    # return JsonResponse(data={"response": 'res'}, safe=True)
    return render(request, 'django_app/home.html', context=context)


def register(request: HttpRequest) -> HttpResponse:
    #

    if request.method == "GET":
        context = {}
        return render(request, 'django_app/register.html', context=context)
    elif request.method == "POST":

        first_name = request.POST.get('first_name', "")
        last_name = request.POST.get('last_name', "")
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', "")
        password2 = request.POST.get('password2', "")

        if password1 and password1 != password2:
            raise Exception("Passwords don't match!!")
        if username and password1:
            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=make_password(password1),
            )
            return redirect(reverse('django_app:login', args=()))
        else:
            raise Exception("Data isn't filled!")


def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(f"email: {email}")
        print(f"password: {password}")

        with open('static/temp/data.txt', 'w') as file:
            file.write(f"{email}\n")
            file.write(f"{password}\n")
    context = {}
    return render(request, 'django_app/login.html', context=context)


def post_list(request: HttpRequest) -> HttpResponse:
    posts = models.Post.objects.all()  # filter order_by
    context = {"posts": posts}
    return render(request, 'django_app/post_list.html', context=context)


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = models.Post.objects.get(id=pk)
    context = {"post": post}
    return render(request, 'django_app/post_detail.html', context=context)


def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    post = models.Post.objects.get(id=pk)
    post.delete()
    return redirect(reverse('django_app:post_list', args=()))


def post_pk_view(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "GET":
        # post_list = models.Post.objects.all()
        # print(f"post_list: {post_list}")
        # context = {"post_list": post_list}
        context = {}
        return render(request, 'django_app/post_detail.html', context=context)
    context = {}

    # return JsonResponse(data={"response": 'res'}, safe=True)
    return render(request, 'django_app/post_list.html', context=context)


def home_main(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'django_app/home_main.html', context=context)


def post_comment_create(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "POST":
        text = request.POST.get('text', None)
        post = models.Post.objects.get(id=pk)
        models.PostComment.objects.create(
            user=request.User,
            article=post,
            text=text,
            # date_time=timezone.now()
        )
        return redirect(reverse('django_app:post_detail', args=(pk,)))


def post_comment_delete(request: HttpRequest, pk: int) -> HttpResponse:
    comment = models.PostComment.objects.get(id=pk)
    pk = comment.article.id
    comment.delete()
    return redirect(reverse('django_app:post_detail', args=(pk,)))


def post_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {}
        return render(request, 'django_app/post_create.html', context=context)
    elif request.method == "POST":
        print("request: ", request)
        # print("request.data: ", request.data)
        print("request.POST: ", request.POST)
        print("request.GET: ", request.GET)
        print("request.META: ", request.META)

        title = request.POST.get('title', None)
        description = request.POST.get('description', "")
        post = models.Post.objects.create(
            title=title,
            description=description,
        )
        return redirect(reverse('django_app:post_list', args=()))


def logout_f(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(reverse('django_app:login', args=()))


def profile(request):
    return render(request, 'django_app/profile.html')


def profileupdate(request):
    if request.method == 'POST':
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid:
            pform.save()
            return render(request, 'django_app/profile.html')
    else:
        pform = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'django_app/profileupdate.html', {'pform': pform})


def json_page(request):
    users = [{"name": f"AnyName ({x})", "age": x} for x in range(1, 8)]
    print(users)

    return JsonResponse({"Your information": users})


def todo_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {}
        return render(request, 'django_app/todo_create.html', context=context)
    elif request.method == "POST":
        print("request: ", request)
        print("request.POST: ", request.POST)
        print("request.GET: ", request.GET)
        print("request.META: ", request.META)

        title = request.POST.get('title', "")
        description = request.POST.get('description', "")
        todo = models.Todo.objects.create(
            title=title,
            description=description,
        )
        return redirect(reverse('django_app:todo_list', args=()))


class CustomPaginator:
    @staticmethod
    def paginate(object_list: any, per_page=5, page_number=1):
        paginator_instance = Paginator(object_list=object_list, per_page=per_page)
        try:
            page = paginator_instance.page(number=page_number)
        except PageNotAnInteger:
            page = paginator_instance.page(number=1)
        except EmptyPage:
            page = paginator_instance.page(number=paginator_instance.num_pages)
        return page


def todo_list(request: HttpRequest) -> HttpResponse:
    todos = models.Todo.objects.all()

    selected_page_number = request.GET.get('page', 1)
    selected_limit_objects_per_page = request.GET.get('limit', 3)
    if request.method == "POST":
        selected_page_number = 1
        selected_limit_objects_per_page = 9999
        search_by_title = request.POST.get('search', None)
        if search_by_title is not None:
            todos = todos.filter(title__contains=str(search_by_title))
        filter_by_user = request.POST.get('filter', None)
        if filter_by_user is not None:
            todos = todos.filter(user=User.objects.get(username=filter_by_user))
    page = CustomPaginator.paginate(
        object_list=todos, per_page=selected_limit_objects_per_page, page_number=selected_page_number
    )

    context = {"page": page, "users": User.objects.all()}
    return render(request, 'django_app/todo_list.html', context=context)


def todo_delete(request: HttpRequest, pk: int) -> HttpResponse:
    todo = models.Todo.objects.get(id=pk)
    todo.delete()
    return redirect(reverse('django_app:todo_list', args=()))


def controller_test(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'django_app/testcontroller.html', context=context)
