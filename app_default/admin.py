from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date information', {'fields' : ['pub_date']}),
    ]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]

    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin) # django admin page에 DB Model 등록하는 방법

# admin.site.register(Question)