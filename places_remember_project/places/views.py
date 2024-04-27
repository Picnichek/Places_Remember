from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Memory


@login_required
def home(request):
    memories = Memory.objects.filter(user=request.user)
    return render(request, 'places/home.html', {'memories': memories})


@login_required
def add_memory(request):
    if request.method == 'POST':
        ...
    else:
        return render(request, 'places/add_memory.html')


@login_required
def edit_memory(request, memory_id):
    memory = Memory.objects.get(pk=memory_id)
    if request.method == 'POST':
        ...
    else:
        return render(request, 'places/edit_memory.html', {'memory': memory})
