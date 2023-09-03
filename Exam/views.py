from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
import time

# Views

def new(request):
    return index(request)

def index(request):

    if request.method == "POST":
        title = (request.POST["exam_name"]).lower()
        time_st = request.POST["exam_st"]
        time_end = request.POST["exam_end"]
        duration = int(request.POST["duration"])
        description = request.POST["description"]
        user = User.objects.get(username = request.user.username)

        if Exam.objects.filter(title = title, examiner = user).exists():
            messages.info(request, "This Exam exists!")
            return redirect("/")

        else:
            if title == False or time_st == False or time_end == False\
                or duration == False:
                return redirect("/")

            elif duration <= 0:
                return redirect("/")

            else:
                exam = Exam.objects.create(
                    title = title,
                    time_st = time_st,
                    time_end = time_end,
                    duration = duration,
                    description = description,
                    examiner = user
                )
                exam.save()

                return redirect("/myexams")

    return render(request, "index.html")


# Exams / Competitions hosted by User.
def myexams(request):

    user = User.objects.get(username=request.user.username)

    exams_by_user = Exam.objects.filter(examiner=user).order_by("title")

    context = {
        'user': user,
        'exams': exams_by_user
    }

    return render(request, "myexams.html", context)

def addquestion(request, user, title):
    if request.method == "POST":
        new_question = request.POST["new_question"]
        opA = request.POST["opA"]
        opB = request.POST["opB"]
        opC = request.POST["opC"]
        opD = request.POST["opD"]
        answer = request.POST["answer"]

        username = User.objects.get(username=request.user.username)
        exam = Exam.objects.get(title = title, examiner = username)

        question = Question.objects.create(
            exam = exam,
            examiner = request.user.username,
            question = new_question,
            op1 = opA,
            op2 = opB,
            op3 = opC,
            op4 = opD,
            answer = answer
        )
        question.save()

        return redirect("/exam/add/"+str(user)+"/"+title)
    else:
        # username = User.objects.get(username=request.user.username)
        if Exam.objects.filter(title = title).exists():
            if user.lower() == request.user.username:

                context = {
                    "user": user,
                    "title": title
                }

                return render(request, "addquestion.html", context)
            else:
                
                return render(request, "error/not-authorized.html")
        else:
            return render(request, "error/does-not-exist.html")

def questions(request, user, title):
    if request.method == "POST":
        del_question_id = int(request.POST["del_question"])
        question = Question.objects.get(id = del_question_id)
        question.delete()

        return redirect("/exam/questions/"+str(user)+"/"+title)
    else:
        if Exam.objects.filter(title = title).exists():
            if user.lower() == request.user.username:
                exam = Exam.objects.get(title = title)
                questions = Question.objects.filter(examiner = user.lower(), exam = exam)
                context = {
                    "user": user,
                    "title": title,
                    "questions": questions
                }


                return render(request, "questions.html", context)
            else:
                return render(request, "error/not-authorized.html")
        else:
            return render(request, "error/does-not-exist.html")

def editquestion(request, user, title, id):
    if request.method == "POST":
        edit_question = request.POST["edit_question"]
        opA = request.POST["opA"]
        opB = request.POST["opB"]
        opC = request.POST["opC"]
        opD = request.POST["opD"]
        answer = request.POST["answer"]

        update_question = Question.objects.get(id = id, examiner = request.user.username)

        update_question.question = edit_question
        update_question.op1 = opA
        update_question.op2 = opB
        update_question.op3 = opC
        update_question.op4 = opD
        update_question.answer = answer
        update_question.save()

        messages.info(request, "This Question has been updated!")
        return redirect("/exam/edit/"+str(user)+"/"+title+"/"+id)
    else:
        # username = User.objects.get(username=request.user.username)
        if Exam.objects.filter(title = title).exists():
            if user.lower() == request.user.username:
                question = Question.objects.get(id = id)
                context = {
                    "user": user,
                    "title": title,
                    "question": question,
                    # "messages":messages
                }

                return render(request, "editquestion.html", context)
            else:
                
                return render(request, "error/not-authorized.html")
        else:
            return render(request, "error/does-not-exist.html")

def datetime_to_seconds(input_datetime):
    # Convert the input datetime to the specified time zone
    converted_datetime = timezone.localtime(input_datetime)

    # Convert to seconds
    timestamp_seconds = int(converted_datetime.timestamp())
    return timestamp_seconds

def pre_exam(request, user, title):
    examiner = User.objects.get(username = user)
    exam = Exam.objects.filter(title = title, examiner = examiner)
    username = User.objects.get(username = request.user.username)
    done_exam = None
    
    if exam.exists():
        if Results.objects.filter(name = username, exam = exam[0]).exists():
            done_exam = True
            result = Results.objects.get(name = username, exam = exam[0])
                    
        time_st = datetime_to_seconds(exam[0].time_st) 
        time_end = datetime_to_seconds(exam[0].time_end)
        
        if time_st <= time.time():
            if time.time() <= time_end:
                current_time = True
            else:
                current_time =  False
        else:
            current_time = False
        # result = None
        context = {
            "examiner": user,
            "title": title,
            "exam" : exam[0],
            "time_st": time_st,
            "time_end": time_end,
            "time": time.time(),
            "current_time": current_time,
            "done_exam": done_exam,
            "result": result

        }
        return render(request, "pre_exam.html", context)
    else:
        return render(request, "error/does-not-exist.html")

def exam(request, user, title):
    global title_
    global qsts
    title_ = title
    if request.method == "POST":
        examiner = User.objects.get(username = user)
        username = User.objects.get(username = request.user.username)
        exam = Exam.objects.filter(title = title, examiner = examiner)[0]
        if Results.objects.filter(name = username, exam = exam).exists():
            return redirect("/")

        else:

            qsts = Question.objects.filter(examiner = examiner, exam = exam)

            context = {
                "exam": exam,
                "questions": qsts
            }

            return render(request, "exam.html", context)
    else:
        return redirect("/exam/info/"+user+"/"+title)

def result(request):
    global title_
    global qsts
    if request.method == "POST":
        try:
            score = 0
            wrong = 0
            total = 0
            time = timezone.now() 

            for abc in qsts:
                total += 1
                print(request.POST.get(abc.question))
                print(abc.answer)
                if abc.answer == request.POST.get(abc.question):

                    score += 1
                else:
                    wrong+=1

            percentage = round(score/total * 100, 0)
            percentage = str(percentage)[:-2]

            username = User.objects.get(username=request.user.username)
            exam = Exam.objects.get(title = title_, examiner = username)

            result_ = Results.objects.create(
                name = username,
                exam = exam,
                score = percentage
            )
            result_.save()

            context = {
                'score':score,
                'wrong': wrong,
                'total': total,
                'percentage':percentage,
                'time':time
            }

            return render(request, "result.html", context)
        except:
            return redirect("/")
    return redirect("/")

def students_progress(request, user, title):
    examiner = User.objects.get(username = user)
    if Exam.objects.filter(title = title, examiner = examiner).exists():

        if request.user.username == user:
            exam = Exam.objects.get(title = title, examiner = examiner)
            students = Results.objects.filter(name = examiner, exam = exam)

            context = {
                "students": students,
                "exam": exam
            }
            return render(request, "progress.html", context)

        else:
            return render(request, "error/not-authorized.html")
    else:
        return render(request, "error/does-not-exist.html")

def followexams(request):

    username = User.objects.get(username = request.user.username)
    f_exams = Results.objects.filter(name = username)

    context = {
        "f_exams": f_exams
    }

    return render(request, "follow-exams.html", context)

