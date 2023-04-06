from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')


def chat_room(request, room_name):
    return render(request, 'chat/chat_room.html', {
        'room_name': room_name
    })


class HomePageView(TemplateView):
    template_name = 'home.html'

class ServiceWorkerView(TemplateView):
    content_type = 'application/javascript'
    template_name = 'sw.js'

class SignUp(View):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return self.success_url

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        return render(request, self.template_name, {'form': form})