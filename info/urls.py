from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('info_form/', views.info_form),
    path('info_update/', views.info_update),
    path('vaccination_info/', views.vaccination_info),
    path('vaccination_info_form/', views.vaccination_info_form),
    path('notice/', views.notice_list),
    path('notice_form/', views.notice_form),
    path('notice_detail/', views.notice_detail),
    path('notice_update/', views.notice_update),
    path('diary/', views.diary_list),
    path('diary_form/', views.diary_form),
    path('diary_detail/', views.diary_detail),
    path('diary_update/', views.diary_update),
    path('join/', views.member_form),
    path('login/', views.login_form),
    path('logout/', views.logout),
    path('info_delete/', views.info_delete),
    path('diary_delete/', views.diary_delete),
]