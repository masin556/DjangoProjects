from django.urls import path
from .views import game_home

urlpatterns = [
    path('game/', game_home, name='game_home'),
    # 기존의 다른 URL 패턴들을 여기에 추가
]