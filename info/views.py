from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.

#애견 정보
def index(request):
    return render(request, 'info/info.html')

#애견 정보 등록 form
def info_form(request):
    return render(request, 'info/info_form.html')