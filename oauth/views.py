from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    print('test');
    return render(request, 'oauth/oauth.html')
