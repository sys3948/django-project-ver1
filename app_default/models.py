import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # ChaarField는 문자열 타입, max_length 인자는 제약 조건으로 최대길이를 의미한다.
    pub_date = models.DateTimeField('date published') # DateTimeField는 날짜와 시간 형태 타입 인자값인 'date published'의미는 사람이 읽기ㅏ 쉬운 형태를 사용한다라는 의미이다.

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 왜래키 필드인 ForeignKey다. 인자값으로 참조할 객체(Table, Class)를 의미, 쉽게 설명하면 소속될 상대 객체를 의미한다. on_delete 인자는 상위 TB의 데이터를 삭제했을 시 해당 TB의 데이터 삭제에 대한 여부를 의미하는 인자다.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text