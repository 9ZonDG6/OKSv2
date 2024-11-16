from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from WebsiteBuilder import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("", include("WebsiteBuilder.urls")),
    path("", include("Hosting.urls")),
    path("", include("Usersite.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        "/Usersite/", document_root=settings.BASE_DIR / "templates/Usersite"
    )
