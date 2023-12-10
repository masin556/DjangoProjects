from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question



@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴받는다.
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


# 질문 수정
# Edit question
@login_required(login_url='common:login')  # 로그인이 필요한 상태에서만 접근 가능
def question_modify(request, question_id):
    # 주어진 question_id에 해당하는 Question 객체를 가져오거나 404 에러를 발생시킴
    question = get_object_or_404(Question, pk=question_id)
    
    # 현재 사용자가 해당 질문의 저자가 아니면 권한이 없다는 에러 메시지를 띄우고 상세 페이지로 리다이렉트
    if request.user != question.author:
        messages.error(request, 'You do not have permission to edit')
        return redirect('pybo:detail', question_id=question.id)
    
    # HTTP 요청이 POST 방식인 경우
    if request.method == "POST":
        # POST 데이터와 현재 question 객체를 사용하여 QuestionForm을 초기화
        form = QuestionForm(request.POST, instance=question)
        
        # 폼이 유효한 경우
        if form.is_valid():
            # 수정된 내용을 저장하되 데이터베이스에는 반영하지 않음(commit=False)
            question = form.save(commit=False)
            
            # 수정일자를 현재 시간으로 갱신
            question.modify_date = timezone.now()
            
            # 수정된 내용을 데이터베이스에 저장
            question.save()
            
            # 수정된 질문의 상세 페이지로 리다이렉트
            return redirect('pybo:detail', question_id=question.id)
    
    # HTTP 요청이 POST 방식이 아닌 경우 (첫 진입 시)
    else:
        # 현재 question 객체를 사용하여 QuestionForm을 초기화
        form = QuestionForm(instance=question)
    
    # 폼 객체를 context에 담아 템플릿으로 전달
    context = {'form': form}
    
    # 질문 수정 폼 템플릿을 렌더링
    return render(request, 'pybo/question_form.html', context)


# 삭제 버튼 정의
@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')



# 질문 추천 버튼
@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)
