import os

from django.db import models
from OKS import settings


def upload_to_domen(instance, filename):
    return os.path.join("Usersite", instance.domen_name, filename)


class Hosting(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="hostings",
    )
    title = models.CharField(verbose_name="Название запроса", max_length=100)
    domen_name = models.CharField(verbose_name="Домен второго уровня", max_length=100)
    file_html = models.FileField(verbose_name="HTML файл", upload_to=upload_to_domen)
    file_css = models.FileField(
        verbose_name="CSS файл",
        upload_to=upload_to_domen,
        blank=True,
        null=True,
    )
    status = models.BooleanField(verbose_name="Статс заявки", default=False)

    class Meta:
        ordering = ["-status"]
        verbose_name = "Hosting"
        verbose_name_plural = "Hostings"

    def __str__(self):
        return self.title
