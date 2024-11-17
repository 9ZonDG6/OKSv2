import os
from django.conf import settings
from django.http import Http404
from django.template.response import TemplateResponse
from Hosting.models import Hosting


def render_dynamic_page(request, directory):
    try:
        hosting = Hosting.objects.get(domen_name=directory)
    except Hosting.DoesNotExist:
        raise Http404("Домен не найден")

    if not hosting.status:
        return TemplateResponse(
            request,
            "error.html",
            {"message": "Этот сайт недоступен. Заявка еще не одобрена."},
        )

    template_path = os.path.join(
        settings.MEDIA_ROOT, "Usersite", directory, "index.html"
    )
    if not os.path.exists(template_path):
        raise Http404("Шаблон не найден")

    return TemplateResponse(request, template_path, {"directory": directory})
