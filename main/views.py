from django.shortcuts import render
from django.http import HttpResponse

#def home(request):
#    return HttpResponse("Hello, World")

def home(request):
    return render(request,  "main/home.html",{'message':'Hi, there__!'})