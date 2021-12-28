from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6
    # template_name = 'bookmark/bookmark_list.html'


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] # 어떤 필드들을 입력받을 것인지 설정하는 부분.
    success_url = reverse_lazy('list') # 글 작성 완료후 이동할 페이지
    template_name_suffix = '_create'
    # template_name = 'bookmark/bookmark_create.html'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')