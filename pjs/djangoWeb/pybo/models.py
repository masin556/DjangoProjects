from django.db import models

# 제목, 내용, 작성일시 
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField() 
    
    def __str__(self):
        return self.subject

# 질문에 대한 답변 Question모델을 속성으로 가져간다. 
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()