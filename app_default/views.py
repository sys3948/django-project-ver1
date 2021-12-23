from django.db import models
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'app_default/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published question."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'app_default/detail.html'


class ResultsView(generic.DeleteView):
    models = Question
    template_name = 'app_default/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        pass
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app_default/default.html', {
            'question' : question,
            'error_message' : "You didn't select a choice",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('app_default:result', args={question.id,}))