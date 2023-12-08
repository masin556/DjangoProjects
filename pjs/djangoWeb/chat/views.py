from django.shortcuts import render
from django.views.generic import ListView
from .models import ChatMessage

def home(request):
    return render(request, 'home.html')

class ChatHistoryView(ListView):
    model = ChatMessage
    template_name = 'chat/chat_history.html'
    context_object_name = 'chat_messages'
    ordering = ['-timestamp']