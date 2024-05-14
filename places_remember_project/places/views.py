from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Memory
from .forms import MemoryForm
from django.conf import settings

url = "https://api-maps.yandex.ru/2.1/?apikey=" + settings.YANDEX_MAPS_API_KEY + "&lang=ru_RU"


@login_required
def home(request):
    memories = Memory.objects.filter(user=request.user)
    return render(request, 'places/home.html', {'memories': memories})


@login_required
def add_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            return redirect('places:home')
    form = MemoryForm()
    return render(request, 'places/add_memory.html', {'form': form, 'url': url})


@login_required
def edit_memory(request, memory_id):
    memory = get_object_or_404(Memory, pk=memory_id)
    if memory.user != request.user:
        return redirect('home')
    if request.method == 'POST':
        form = MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            form.save()
            return redirect('places:home')
    form = MemoryForm(instance=memory)
    return render(request, 'places/edit_memory.html', {'form': form, 'memory': memory, 'url': url})


@login_required
def delete_memory(request, memory_id):
    memory = get_object_or_404(Memory, pk=memory_id)
    if memory.user != request.user:
        return redirect('home')
    if request.method == 'POST':
        memory.delete()
        return redirect('places:home')
    return render(request, 'places/delete_memory.html', {'memory': memory, 'url': url})
