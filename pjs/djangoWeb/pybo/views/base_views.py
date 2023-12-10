from django.core.paginator import Paginator  
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponseNotAllowed
from ..models import Question, Answer

#pybo\question_list.html
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    # ('-create_date') 역순으로 정렬 | order_by는 조회 결과를 정렬하는 함수
    question_list = Question.objects.order_by('-create_date') 
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    # 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
    return render(request, 'pybo/question_list.html', context)


#pybo\question_detail.html
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


# home 링크
def redirect_to_external_link(request):
    external_link = "https://gibeonsoftworks.notion.site/GIBEON-GAME-STUDIO-Customer-c412c9b24b7d4f2183396cdd3572e054?pvs=4"
    return redirect(external_link)

# Gmae 링크
def game_home(request):
    # game_home 뷰 함수의 내용 추가
    return render(request, 'pybo/game_home.html')  # 예시로 'pybo/game_home.html'을 렌더링하도록 함

#Profile
@login_required(login_url='common:login')
def profile(request):
    return render(request, 'pybo/profile.html')

