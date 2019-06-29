from django.http import HttpResponse
from django.shortcuts import render
import logging
import requests
# Create your views here.

#애견 정보
def index(request):
    return render(request, 'info/info.html')

#애견 정보 등록 form
def info_form(request):
    logger = logging.getLogger('')
    logger.error('로그찍기')
    return render(request, 'info/info_form.html')