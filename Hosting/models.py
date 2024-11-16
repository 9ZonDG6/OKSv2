from django.db import models
from OKS import settings


class Hosting(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="hostings",
    )
    title = models.CharField(verbose_name="Название запроса", max_length=100)
    domen_name = models.CharField(verbose_name="Домен", max_length=100)
    file_html = models.FileField(
        verbose_name="HTML файл", upload_to="hosting/html/%Y/%m/%d/"
    )
    file_css = models.FileField(
        verbose_name="CSS файл",
        upload_to="hosting/css/%Y/%m/%d/",
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
