from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.contrib.auth import login


def home(request):
    return render(request, "WebsiteBuilder/home.html")


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "WebsiteBuilder/register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password"])
            user.save()

            login(request, user)

            return redirect("home")
        return render(request, "WebsiteBuilder/register.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "WebsiteBuilder/login.html"
    redirect_authenticated_user = True


@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        return render(
            request, "WebsiteBuilder/profile.html", {"form": form, "user": request.user}
        )

    def post(self, request):
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("WebsiteBuilder:profile")  # Updated line
        return render(
            request, "WebsiteBuilder/profile.html", {"form": form, "user": request.user}
        )
