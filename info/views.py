from datetime import datetime

from django.utils.dateformat import DateFormat


from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import render
import logging
import requests
from django.views.decorators.csrf import csrf_exempt

from .models import dogda_vaccination_info, dogda_info, notice, diary, member
from .forms import Dogda_infoForm,Dogda_vaccination_infoForm, noticeForm, diaryForm, memberForm
from django.shortcuts import get_object_or_404

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

    if request.method == "POST":
        dict = request.POST.dict()

        dogda_birth = request.POST.get('dogda_birth')

        print(dogda_birth)
        dict["reg_date"] = date
        dict["dogda_birth"] = dogda_birth.replace("-", "")

        print(dict)

        form = Dogda_infoForm(dict)

        if form.is_valid():
            dogda_info = form.save(commit=False)
            dogda_info.save()
            return HttpResponseRedirect("/info")

    else:

        logger = logging.getLogger('')
        logger.error('로그찍기')

        return render(request, 'info/info_form.html')

#애견정보 업데이트
def info_update(request):
    if request.method == "GET":

        id = request.GET.get("id")
        dogda_name = request.GET.get("dogda_name")
        info_list = dogda_info.objects.get(id=id, dogda_name=dogda_name)

        birth1 = str(info_list.dogda_birth[0:4])
        birth2 = str(info_list.dogda_birth[4:6])
        birth3 = str(info_list.dogda_birth[6:10])

        info_list.dogda_birth = birth1+"-"+birth2+"-"+birth3
        print(info_list.dogda_birth)
        data = {
            'dogda_name': info_list.dogda_name,
            'id': info_list.id,
            'dogda_type': info_list.dogda_type,
            'dogda_birth': info_list.dogda_birth,
            'dogda_gender' : info_list.dogda_gender,
            'idx' : info_list.idx
        }

        print(data)

        return render(request, 'info/info_update.html', data)
    else:

        id = request.POST.get("id")
        idx = request.POST.get("idx")
        dogda_birth = request.POST.get("dogda_birth")
        dogda_name = request.POST.get("dogda_name")
        dogda_gender = request.POST.get("dogda_gender")
        dogda_type = request.POST.get("dogda_type")

        print(dogda_name);
        dict = {
            'dogda_name': dogda_name,
            'id': id,
            'dogda_birth': dogda_birth.replace("-", ""),
            'dogda_gender': dogda_gender,
            'dogda_type' : dogda_type
        }

        list = dogda_info.objects.filter(id='pizzu', idx=idx).values()
        print(list)
        dogda_info.objects.filter(id='pizzu', idx=idx).update(**dict)
        return HttpResponseRedirect("/info")

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

def notice_detail(request):
    idx = request.GET.get("idx")


    notice_list = notice.objects.get(idx=idx)

    data = {
        'list' : notice_list
    }
    print(notice_list.title)

    return render(request, 'info/notice_detail.html', data)

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

        cal_date = cal_date[:-1]
        cal_date = cal_date.replace("년","-");
        cal_date =  cal_date.replace("월","-");


        data = {
            'reg_date' : cal_date
        }

        print(data)

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
        logger = logging.getLogger('')
        logger.error('로그찍기')

        return render(request, 'info/diary_detail.html')

# 회원가입
@csrf_exempt
def member_form(request):

    # data = request.POST
    date = DateFormat(datetime.now()).format('Y-m-d')  # 오늘 날짜만 가져오기

    if request.method == "POST":
        dict = request.POST.dict()
        dict['reg_date'] = date

        print(dict)
        form = memberForm(dict)

        if form.is_valid():
            dogda_member = form.save(commit=False)
            dogda_member.save()
            return HttpResponseRedirect("/info/login")

    else:

        logger = logging.getLogger('')
        logger.error('로그찍기')
        return render(request, 'login/join_form.html')

# 로그인
@csrf_exempt
def login_form(request):

    if request.method == "POST":

        try:
            list = member.objects.get(id=request.POST.get('id'))
            if list is not None:
                print("list")
                request.session['id'] = list.id
                return HttpResponseRedirect("/info")
            else:
                print("a")
                return render(request, 'login/login_form.html')
            #    return render(request, 'account/login.html', {'error': 'username or password is incorrect'})
        except member.DoesNotExist:
            list = None
            return render(request, 'login/login_form.html')



    else:
        logger = logging.getLogger('')
        logger.error('로그찍기')
        request.session.get('id')
        return render(request,'login/login_form.html')

# 로그인
@csrf_exempt
def logout(request):

    if request.method == "GET":

        del request.session['id']

        return HttpResponseRedirect("/info")
