from django.db import models
from django.dispatch import receiver
from django.contrib.auth import user_logged_in
from django.contrib.auth.models import AbstractUser
from .services import update_user_photo_from_vk


@receiver(user_logged_in)
def update_user_photo(sender, request, user, **kwargs):
    if user.username != 'admin':
        update_user_photo_from_vk(user)


class CustomUser(AbstractUser):
    photo_max = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username
