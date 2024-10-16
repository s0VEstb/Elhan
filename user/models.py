from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username