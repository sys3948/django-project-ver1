from django.contrib import admin

# Register your models here.

from .models import Question, Choice

admin.site.register(Question) # django admin page에 DB Model 등록하는 방법