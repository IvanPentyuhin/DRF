from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=110, unique=True)
