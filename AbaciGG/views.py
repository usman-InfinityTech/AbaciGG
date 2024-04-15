from django.shortcuts import render


def index(request):
    return render(request, template_name="website/index.html")


def about_us(request):
    return render(request, template_name="website/about_us.html")