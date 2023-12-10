from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from django.http import HttpResponse

@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    context = {'user_profile': user_profile}
    return render(request, 'profiles/user_profile.html', context)

@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # 프로필 수정 로직을 여기에 추가
        # ...

        return HttpResponse('프로필이 수정되었습니다.')  # 수정 성공 시 응답

    context = {'user_profile': user_profile}
    return render(request, 'profiles/edit_profile.html', context)
