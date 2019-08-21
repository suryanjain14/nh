from django.shortcuts import render,redirect
from .models import Question,Answer
from .forms import Question_form,Answer_form


def index(request):
    if request.method =="POST":
       u_form= Question_form(request.POST or None,request.FILES or None)
       if u_form.is_valid():
           u_form.save(commit=False)
           u_form.posted_by=request.user
           u_form.save()
           questions=Question.objects.all()
           u_form = Question_form(request.POST, request.FILES)
           context = {'questions': questions,'u_form':u_form}
           return render(request,"qna/index.html",context)
       else:
           questions = Question.objects.all()
           error="something is wrong in the form"
           u_form = Question_form(request.POST, request.FILES)
           context = {'questions': questions, 'u_form': u_form,'error':error}
           return render(request, "qna/index.html", context)
    else:
        questions = Question.objects.all()

        u_form=Question_form(request.POST,request.FILES)
        context = {'questions': questions,'u_form':u_form}
        return render(request, "qna/index.html", context)




