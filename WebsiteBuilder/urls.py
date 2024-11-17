from django.conf import settings
from django.urls import path
from WebsiteBuilder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path(
        "logout/",
        LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),
        name="logout",
    ),
]
