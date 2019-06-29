from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('info_form/', views.info_form),

]