from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Choice, Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'app_default/index.html', context) # loder함수를 이용해서 template을 출력하는 방식말고 render 함수로 사용하여 편리하게 응답하기.


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # 404 error를 발생시키기 위해서는 Http404객체를 사용해야한다. 그러나 그 방법보다 더 편한 객체(get_object_or_404)를 이용하는 방법.
    return render(request, 'app_default/detail.html', {'question' : question})


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app_default/result.html', {'question' : question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app_default/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))