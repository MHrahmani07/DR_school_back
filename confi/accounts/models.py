from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'مدیر'
        DEPUTY = 'deputy', 'معاون'

    role = models.CharField(
        max_length=10, 
        choices=Role.choices, 
        default=Role.DEPUTY
        )
    phone_number = models.CharField(max_length=15, blank=True)

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def __str__(self):
        return self.get_full_name() or self.username