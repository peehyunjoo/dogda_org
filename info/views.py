from datetime import datetime

from django.utils.dateformat import DateFormat


from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import render
import logging
import requests
from django.views.decorators.csrf import csrf_exempt

from .forms import Dogda_infoForm
from .models import dogda_info
# Create your views here.

#애견 정보
def index(request):
    return render(request, 'info/info.html')

#애견 정보 등록 form
@csrf_exempt
def info_form(request):

    # data = request.POST
    date = DateFormat(datetime.now()).format('Y-m-d')     #오늘 날짜만 가져오기

    dict = request.POST.dict()
    dict["reg_date"] = date

    print(dict)
    if request.method == "POST":
        form = Dogda_infoForm(dict)

        if form.is_valid():
            dogda_info = form.save(commit=False)
            dogda_info.save()
            return render(request, 'info/info.html')

    else:

        logger = logging.getLogger('')
        logger.error('로그찍기')
        return render(request, 'info/info_form.html')
