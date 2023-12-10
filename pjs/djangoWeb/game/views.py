# game/views.py
from django.shortcuts import render

def _game(request):
    # 체스 게임을 렌더링하는 뷰 함수
    return render(request, 'game/_game.html')
