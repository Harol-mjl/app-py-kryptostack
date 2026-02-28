from django.db import models

class UserRoleChoices(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    EDITOR = 'EDITOR', 'Editor'
    SUPER_USER = 'SUPER_USER', 'Super User'
    STAFF = 'STAFF', 'Staff'
    GUEST = 'GUEST', 'Guest'
