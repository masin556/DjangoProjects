from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    # 다른 URL 패턴들도 필요하다면 추가
]