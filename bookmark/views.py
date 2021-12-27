from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    template_name = 'bookmark/bookmark_list.html'