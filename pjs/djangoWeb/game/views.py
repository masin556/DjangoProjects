from django.shortcuts import render

# Create your views here.

#def home(request):
    #items = HomeItem.objects.all()
    #return render(request, 'home/home.html', {'items': items})


def game_home(request):
    # 게임 홈 뷰의 내용
    return render(request, 'game/game_home.html')