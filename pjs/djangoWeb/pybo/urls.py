# config/urls.py  에 매핑 정보를 전달해주는 urls.py이다

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]