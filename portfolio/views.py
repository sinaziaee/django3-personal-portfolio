from django.shortcuts import render
from .models import App


def home(request):
    apps = App.objects.all()
    return render(request, 'portfolio/home.html', {'apps': apps})
