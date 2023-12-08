from django.urls import path
from .views import home, ChatHistoryView

urlpatterns = [
    path('', home, name='home'),
    path('chat/', ChatHistoryView.as_view(), name='chat_history'),
]