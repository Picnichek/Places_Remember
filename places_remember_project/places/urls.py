from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_memory/', views.add_memory, name='add_memory'),
    path('edit_memory/<int:memory_id>/', views.edit_memory, name='edit_memory'),
    path('delete_memory/<int:memory_id>/',
         views.delete_memory, name='delete_memory'),
]
