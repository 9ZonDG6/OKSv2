from django import forms
from Hosting.models import Hosting


class HostingRequestForm(forms.ModelForm):
    class Meta:
        model = Hosting
        fields = ["title", "domen_name", "file_html", "file_css"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "domen_name": forms.TextInput(
                attrs={"class": "form-control", "required": True}
            ),
            "file_html": forms.ClearableFileInput(
                attrs={"class": "form-control", "required": True}
            ),
            "file_css": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean_file_html(self):
        file_html = self.cleaned_data.get("file_html")
        if file_html:
            if not file_html.name.endswith(".html"):
                raise forms.ValidationError("Файл должен быть в формате HTML.")
            if file_html.content_type != "text/html":
                raise forms.ValidationError("Недопустимый тип файла HTML.")
        return file_html

    def clean_file_css(self):
        file_css = self.cleaned_data.get("file_css")
        if file_css:
            if not file_css.name.endswith(".css"):
                raise forms.ValidationError("Файл должен быть в формате CSS.")
            if file_css.content_type != "text/css":
                raise forms.ValidationError("Недопустимый тип файла CSS.")
        return file_css
