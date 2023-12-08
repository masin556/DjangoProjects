from django.shortcuts import render, get_object_or_404
from .models import Question


#pybo\question_list.html
def index(request):
    # ('-create_date') 역순으로 정렬 | order_by는 조회 결과를 정렬하는 함수
    question_list = Question.objects.order_by('-create_date') 
    context = {'question_list': question_list}
    # 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
    return render(request, 'pybo/question_list.html', context)


#pybo\question_detail.html
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


