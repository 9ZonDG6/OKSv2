from django.shortcuts import render


def render_dynamic_page(request, directory):
    template_path = f"Usersite/{directory}/index.html"
    return render(request, template_path)
