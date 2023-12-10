# config/urls.py  에 매핑 정보를 전달해주는 urls.py이다

from django.urls import path, include
from . import views

#url 별칭 사용시 중복방지
app_name = 'pybo'

#name 을 붙여 해당 하는 것에 별칭을 정해줄 수 있다. 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), 
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'), #질문 수정
    path('home/', views.redirect_to_external_link, name='external_home'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('chat/', include('chat.urls')),
    path('game/', views.game_home, name='game_home'),
    path('picture/', include('picture.urls')),
]
