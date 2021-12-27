from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        # 객체를 출력할 때 나타날 값. 해당 메서드의 반환 값은 무조건 str 타입이여야한다.
        return "이름 : " + self.site_name + ", 주소 : " + self.url