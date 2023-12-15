from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    # return HttpResponse('<h2>Home page</h2>')
    return render(req, 'home.html')