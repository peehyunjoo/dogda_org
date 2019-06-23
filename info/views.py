from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.

#정보
def index(request):
    return render(request, 'info/info.html')