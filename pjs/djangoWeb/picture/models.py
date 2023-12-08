from django.db import models

class Picture(models.Model):
    image = models.ImageField(upload_to='pictures/')
    hashtag = models.CharField(max_length=50)

    def __str__(self):
        return f"Picture {self.id}"