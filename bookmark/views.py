from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Bookmark

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    # template_name = 'bookmark/bookmark_list.html'


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] # 어떤 필드들을 입력받을 것인지 설정하는 부분.
    success_url = reverse_lazy('list') # 글 작성 완료후 이동할 페이지
    template_name_suffix = '_create'
    # template_name = 'bookmark/bookmark_create.html'