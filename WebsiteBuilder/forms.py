from datetime import date
from django import forms
from WebsiteBuilder.models import User
from django.core.exceptions import ValidationError
import datetime


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль",
        help_text="Пароль должен содержать минимум 8 символов",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput, label="Подтверждение пароля"
    )

    class Meta:
        model = User
        fields = ("username", "last_name", "birth_date", "email")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise ValidationError("Пароль должен быть не менее 8 символов.")
        return password

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        return password

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birth_date")
        if birth_date:
            age = (date.today() - birth_date).days // 365
            if birth_date > datetime.date.today():
                raise ValidationError("Дата рождения не может быть в будущем.")
            elif age < 18:
                raise forms.ValidationError(
                    "Регистрация доступна только для пользователей старше 18 лет."
                )
            elif age > 100:
                raise forms.ValidationError("Укажите настоящий возраст.")
        return birth_date

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "last_name"]
