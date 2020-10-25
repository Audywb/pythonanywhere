from django.contrib import admin

from .models import Question, Choice, Comment2

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Comment2)