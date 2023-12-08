from django.urls import path
from .views import picture_home

urlpatterns = [
    path('picture/', picture_home, name='picture_home'),
    # 기존의 다른 URL 패턴들을 여기에 추가
]