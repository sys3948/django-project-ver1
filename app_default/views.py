from django.db import models
from django.http.response import HttpResponseRedirect
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