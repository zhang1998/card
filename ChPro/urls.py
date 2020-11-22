from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views


app_name='ChPro'
#from django.conf.urls import url,include
urlpatterns = [
    #re_path('',views.testReturnText,name="homeCo"),
    path('returnText',views.returnText,name='returnText'),
    path('returnQue',views.returnQue,name='returnQue'),
    re_path(r'^questions',views.getQuestions,name='questions'),
    #    re_path(r'^base',views.testbase,name='testbase'),
    re_path('',views.homeCo,name="homeCo"),


]
