from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'app_default/index.html', context) # loder함수를 이용해서 template을 출력하는 방식말고 render 함수로 사용하여 편리하게 응답하기.


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist") # 해당 DB내의 데이터가 존재하지 않을 경우 404 error를 발생해라!
    return render(request, 'app_default/detail.html', {'question' : question})


def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)