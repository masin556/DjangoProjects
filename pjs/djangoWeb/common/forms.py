#회원가입

from django import forms
#UserCreationForm 클래스를 상속하여 만들어진다.
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
