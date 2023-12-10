from django.urls import path
from . import views

urlpatterns = [
    # 여기에 프로필 앱의 URL 패턴을 추가
    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),
    # 다른 URL 패턴을 추가할 수 있음
]

# urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your existing URL patterns here
]

# Add this line at the end of the file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
