import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # ChaarField는 문자열 타입, max_length 인자는 제약 조건으로 최대길이를 의미한다.
    pub_date = models.DateTimeField('date published') # DateTimeField는 날짜와 시간 형태 타입 인자값인 'date published'의미는 사람이 읽기 쉬운 형태를 사용한다라는 의미이다.

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date' # 원칙적으로 임의의 메서드에 의한 값은 정렬이 불가능. 대신 다른 값을 기준으로 정렬할 수 있는데 이 기준 항목을 설정하는 항목
    was_published_recently.boolean = True # 값이 불리언 값 형태인지 설정. True 설정하면 값 대신 아이콘이 나타난다.
    was_published_recently.short_description = 'Published recently?' # 항목의 헤더 이름을 설정


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 왜래키 필드인 ForeignKey다. 인자값으로 참조할 객체(Table, Class)를 의미, 쉽게 설명하면 소속될 상대 객체를 의미한다. on_delete 인자는 상위 TB의 데이터를 삭제했을 시 해당 TB의 데이터 삭제에 대한 여부를 의미하는 인자다.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text