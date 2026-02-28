from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.choices import UserRoleChoices

class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRoleChoices.choices,
        default=UserRoleChoices.EDITOR
    )
    phone = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    def __str__(self):
        return f'{self.full_name} ({self.role})'