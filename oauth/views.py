from django.shortcuts import render
import requests
# Create your views here.

#메인
def index(request):
    return render(request, 'oauth/oauth.html')