from django.contrib import admin
from Hosting.models import Hosting


@admin.register(Hosting)
class HostingAdmin(admin.ModelAdmin):
    list_display = ("title", "domen_name", "status", "file_html", "file_css")
    list_filter = ("status",)
    search_fields = ("title", "domen_name")
    readonly_fields = ("file_html", "file_css")
