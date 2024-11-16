from django.urls import re_path
from Usersite import views

urlpatterns = [
    re_path(r"^(?P<directory>[^/]+)/$", views.render_dynamic_page),
]
