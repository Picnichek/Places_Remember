from django.db import models
from users.models import CustomUser


User = CustomUser()


class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    location = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Местоположение')
    comment = models.TextField(
        blank=True, null=True, verbose_name='Комментарий')
    latitude = models.FloatField()
    longitude = models.FloatField()
