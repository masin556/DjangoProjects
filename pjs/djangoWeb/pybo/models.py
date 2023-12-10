from django.db import models
from django.contrib.auth.models import User


# 제목, 내용, 작성일시 
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField() 
    
    def __str__(self):
        return self.subject

# 질문에 대한 답변 Question모델을 속성으로 가져간다. 
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # migrate시 데이터베이스에 null 허용 컬럼으로 생성
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()