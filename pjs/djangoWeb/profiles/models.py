# profiles/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    # 다른 필드들을 추가할 수 있습니다.

    def __str__(self):
        return self.user.username
