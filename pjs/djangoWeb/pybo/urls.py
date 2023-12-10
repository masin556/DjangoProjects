# config/urls.py  에 매핑 정보를 전달해주는 urls.py이다

from django.urls import path, include
from .views import base_views, question_views, answer_views
#from . import views



#url 별칭 사용시 중복방지
app_name = 'pybo'

#name 을 붙여 해당 하는 것에 별칭을 정해줄 수 있다. 
urlpatterns = [
    #path('', views.index, name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
    #path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), 
    #path('question/create/', views.question_create, name='question_create'),
    #path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'), #질문 수정
    #path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    #path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'), # 답변 수정 -> Views
    #path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'), # 답변 삭제
    
    # 외부 링크로 리다이렉트하는 경로
    path('home/', base_views.redirect_to_external_link, name='external_home'),

    # chat 앱의 URL을 포함합니다.
    path('chat/', include('chat.urls')),

    # 게임 앱의 홈 화면 경로
    path('game/', base_views.game_home, name='game_home'),

    # picture 앱의 URL을 포함합니다.
    path('picture/', include('picture.urls')),
    # profile 앱의 URL을 포함합니다.
    path('profiles/', include('profiles.urls')),

    # 기본 뷰 함수들의 URL 패턴
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:question_id>/',
         base_views.detail, name='detail'),


    # 질문과 관련된 뷰 함수들의 URL 패턴
    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'), #질문 추천

    # 답변과 관련된 뷰 함수들의 URL 패턴
    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'), #답변 삭제
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
]
