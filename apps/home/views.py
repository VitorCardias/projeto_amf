from django.shortcuts import render
from .models import Home


def home(request):
    query_home = Home.objects.all()

    
    return render(request, "home/index.html", {"home": query_home})