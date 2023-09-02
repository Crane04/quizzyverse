from django.contrib import admin
from .models import *
# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    list_display = ("title", "time_st", "time_end", "duration")

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("exam",)

class ResultAdmin(admin.ModelAdmin):
    list_display = ("name", "exam", "score")

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Results, ResultAdmin)