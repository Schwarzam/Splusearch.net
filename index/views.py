from django.shortcuts import render
from django.http import HttpResponse

## Creating views.

def home(request):
    return render(request, 'index/index.html')
