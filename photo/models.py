from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to = 'photo/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # auto_now_add 인자는 Data가 insert 되었을 때 자동적으로 값을 설정한다.
    updated = models.DateTimeField(auto_now=True) # auto_now 인자는 Data가 Update되었을 때 자동적으로 값을 설정한다.


    class Meta:
        ordering = ['-updated'] # ordering 클래스 변수는 해당 모델의 객체들을 어떤 기준으로 정렬할 것인지 설정하는 옵션으로 -updated 옵션 값은 수정 시간의 내림차순으로 정렬한다.

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])