from django.shortcuts import render

def picture_home(request):
    # Picture 홈 뷰의 내용
    return render(request, 'picture/picture_home.html')