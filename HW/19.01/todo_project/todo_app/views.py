from django.shortcuts import render
from django.http import JsonResponse
from .models import Todo


def get_todos(request):
    todos = Todo.objects.all().values()
    return JsonResponse({'todos': list(todos)})


def create_todo(request):
    text = request.POST.get('text')
    todo = Todo.objects.create(text=text)
    return JsonResponse({'id': todo.id, 'text': todo.text, 'completed': todo.completed})


def toggle_todo(request):
    todo_id = request.POST.get('id')
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return JsonResponse({'completed': todo.completed})


def delete_todo(request):
    todo_id = request.POST.get('id')
    Todo.objects.filter(id=todo_id).delete()
    return JsonResponse({})
