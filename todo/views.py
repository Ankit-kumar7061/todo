from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from django.shortcuts import redirect, render # type: ignore
from .models import Task



def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
