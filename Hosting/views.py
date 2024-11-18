import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from Hosting.models import Hosting
from Hosting.forms import HostingRequestForm
from OKS import settings


@method_decorator(login_required, name="dispatch")
class Template(TemplateView):
    template_name = "WebsiteBuilder/templates.html"


@method_decorator(login_required, name="dispatch")
class BuilderOKS(TemplateView):
    template_name = "WebsiteBuilder/builder.html"


@method_decorator(login_required, name="dispatch")
class VideoLesson(TemplateView):
    template_name = "WebsiteBuilder/videolesson.html"


class HostingView(View):
    template_name = "WebsiteBuilder/hosting.html"

    def get(self, request):
        if request.user.is_staff:
            hostings = Hosting.objects.all()
            form = None
        else:
            hostings = Hosting.objects.filter(user=request.user)
            form = None if hostings.exists() else HostingRequestForm()

        return render(
            request,
            self.template_name,
            {"hostings": hostings, "form": form},
        )

    def post(self, request):
        form = HostingRequestForm(request.POST, request.FILES)
        if form.is_valid():
            hosting_request = form.save(commit=False)
            hosting_request.user = request.user
            hosting_request.status = False
            hosting_request.save()
            messages.success(request, "Ваш запрос успешно отправлен!")
            return redirect("HostingList")
        messages.error(request, "Произошла ошибка. Проверьте введенные данные.")
        hostings = Hosting.objects.filter(user=request.user).first()
        return render(
            request,
            self.template_name,
            {"hostings": [hostings] if hostings else [], "form": form},
        )


class ApproveHostingView(View):
    def post(self, request, pk):
        if request.user.is_staff:
            hosting = get_object_or_404(Hosting, pk=pk)

            # Путь к директории домена
            domain_dir = os.path.join(
                settings.MEDIA_ROOT, "Usersite", hosting.domen_name
            )
            os.makedirs(domain_dir, exist_ok=True)

            # Работа с HTML файлами
            if hosting.file_html:
                html_target = os.path.join(domain_dir, "index.html")
                os.rename(hosting.file_html.path, html_target)
                hosting.file_html.name = os.path.join(
                    "Usersite", hosting.domen_name, "index.html"
                )

            # Работа с CSS файлами
            if hosting.file_css:
                css_target = os.path.join(domain_dir, "styles.css")
                os.rename(hosting.file_css.path, css_target)
                hosting.file_css.name = os.path.join(
                    "Usersite", hosting.domen_name, "styles.css"
                )

            # Обновление статуса
            hosting.status = True
            hosting.save()

            messages.success(
                request,
                f"Заявка '{hosting.title}' была успешно одобрена! Все файлы загружены в '{hosting.domen_name}'.",
            )
        return HttpResponseRedirect(reverse("HostingList"))


class RefuseHostingView(View):
    def post(self, request, pk):
        if request.user.is_staff:
            hosting = get_object_or_404(Hosting, pk=pk)
            hosting.status = False
            hosting.save()
            messages.success(request, f"Заявка '{hosting.title}' была отклонена!")
        return HttpResponseRedirect(reverse("HostingList"))
