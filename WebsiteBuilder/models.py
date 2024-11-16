from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(verbose_name="Имя", max_length=30, unique=True)
    last_name = models.CharField(
        verbose_name="Фамилия", max_length=30, blank=True, null=True
    )
    email = models.EmailField(verbose_name="Email", unique=True)
    avatar = models.ImageField(
        verbose_name="Аватарка", upload_to="avatars/%Y/%m/%d/", blank=True, null=True
    )
    about = models.TextField(verbose_name="О себе", blank=True, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.last_name} {self.username}"
