# Create your views here.
from django.shortcuts import render
from helloworld.models import ClickMe

def user_view(request):
    return render(request, "index.html")

def click_button(request):
    clickMe = ClickMe()
    clickMe.save()
    return render(request, "index.html")