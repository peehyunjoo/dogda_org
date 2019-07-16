from datetime import datetime

from django.utils.dateformat import DateFormat


from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import render
import logging
import requests
from django.views.decorators.csrf import csrf_exempt

from .models import dogda_vaccination_info, dogda_info, notice, diary
from .forms import Dogda_infoForm,Dogda_vaccination_infoForm, noticeForm, diaryForm

# Create your views here.

#애견 정보
def index(request):
    dogda_info_list = dogda_info.objects.filter(id='pizzu').values()

    print(dogda_info_list)

    data = {
        'list' : dogda_info_list
    }
    return render(request, 'info/info.html' , data)

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
            return HttpResponseRedirect("/info")

    else:

        logger = logging.getLogger('')
        logger.error('로그찍기')
        return render(request, 'info/info_form.html')

#백신 정보
def vaccination_info(request):
    vaccination_info_list = dogda_vaccination_info.objects.filter(id='pizzu').values()

    print(vaccination_info_list)
    data = {
        'list': vaccination_info_list
    }
    print(data)

    return render(request, 'info/vaccination_info.html', data)


#백신 정보 등록 form
@csrf_exempt
def vaccination_info_form(request):

    if request.method == "POST":

        date = DateFormat(datetime.now()).format('Y-m-d')  # 오늘 날짜만 가져오기

        vaccination_date = request.POST.get("vaccination_date")

        vaccination_date = vaccination_date.replace("-", "")
        dict = request.POST.dict()
        dict["reg_date"] = date
        dict["vaccination_date"] = vaccination_date

        print(dict)

        form = Dogda_vaccination_infoForm(dict)

        if form.is_valid():
            dogda_vaccination = form.save(commit=False)
            dogda_vaccination.save()
            return HttpResponseRedirect("/info/vaccination_info")

    else:
        return render(request, 'info/vaccination_info_form.html')

def notice_list(request):       #모델과 view의 이름이 같으면 안되는것같음..
    list = notice.objects.all()
    print(list)
    data = {
        'list': list
    }
    return render(request, 'info/notice.html', data)

@csrf_exempt
def notice_form(request):

    if request.method == "POST":

        form = noticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            return HttpResponseRedirect("/info/notice")
    else:
        return render(request, 'info/notice_form.html')

def diary_list(request):

    diary_list = diary.objects.all()

    print(diary_list)
    data = {
        'list': diary_list
    }

    return render(request, 'info/diary.html',data)

@csrf_exempt
def diary_form(request):
    if request.method == "POST":


        form = diaryForm(request.POST)

        print(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
            return HttpResponseRedirect("/info/diary")
    else:
        cal_date = request.GET.get("cal_date")
        data = {
            'data' : cal_date
        }
        return render(request, 'info/diary_form.html', data)