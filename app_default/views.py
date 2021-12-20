from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('app_default/index.html') # 생성한 template을 불러오는 함수다. default path는 views.py가 존재하는 폴더 내의 templates폴더를 root로 한다.
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request)) # render 함수를 이용하여 template(index.html)에 데이터를 전송한다. 전송하는 구조는 dict다. -> dict의 key가 template 변수가 되는거다.


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." %question_id)


def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)