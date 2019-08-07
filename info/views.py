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

def diary_detail(request):
    reg_date = request.GET.get("reg_date")

    '''
    list = diary.objects.filter(id='pizzu', reg_date = reg_date).values()   #전체 리스트를 가지고오는 것이므로 값만 하나씩 출력할수없음
    
    값을 하나씩 출력하고싶을때는 아래와 같은 방법으로 가져와야함
        list3 = diary.objects.filter(id='pizzu', reg_date=reg_date)
        print(list3[0].id)    ->list타입

        list2 = diary.objects.get(id='pizzu', reg_date=reg_date)
        print(list2.id)        ->dict타입
    '''

    list = diary.objects.get(id='pizzu', reg_date=reg_date)      #값을 가공해야할때는 filter가 아닌 get으로 가져와야 가공할수있는듯
    list.reg_date = str(list.reg_date)

    data = {
        'list': list
    }
    print(type(list))

    return render(request, 'info/diary_detail.html', data)

@csrf_exempt
def diary_update(request):

    reg_date = str(request.POST.get("reg_date"))
    dogda_name = request.POST.get("dogda_name")
    title = request.POST.get("title")
    content = request.POST.get("content")
    flowers = request.POST.get("flowers")

    print(request.POST)

    if request.method == "POST":


            dict = {
                'dogda_name' : dogda_name,
                'title' : title,
                'content' : content,
                'flowers' : flowers
            }

            list = diary.objects.filter(id='pizzu',reg_date = reg_date).values()
            print(list)
            diary.objects.filter(id ='pizzu', reg_date = reg_date).update(**dict)
            return HttpResponseRedirect("/info/diary")

    else:
        print('ss')
        logger = logging.getLogger('')
        logger.error('로그찍기')
        return render(request, 'info/diary_detail.html')