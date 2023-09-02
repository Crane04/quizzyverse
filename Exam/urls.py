from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("new", views.new),
    path("myexams", views.myexams),
    path("exam/add/<str:user>/<str:title>", views.addquestion),
    path("exam/questions/<str:user>/<str:title>", views.questions),
    path("exam/edit/<str:user>/<str:title>/<str:id>", views.editquestion),
    path("exam/info/<str:user>/<str:title>", views.pre_exam),
    path("exam/<str:user>/<str:title>", views.exam),
    path("result", views.result),
    path("followexams", views.followexams),
    path("exam/progress/<str:user>/<str:title>", views.students_progress),
    
]