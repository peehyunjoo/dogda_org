from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('info_form/', views.info_form),
    path('vaccination_info/', views.vaccination_info),
    path('vaccination_info_form/', views.vaccination_info_form),

]