# config/urls.py  에 매핑 정보를 전달해주는 urls.py이다

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
    path('home/', include('home.urls')),
    path('chat/', include('chat.urls')),
    path('game/', include('game.urls')),
    path('picture/', include('picture.urls')),
]
d