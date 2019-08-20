from django.shortcuts import render,redirect
from .models import Question,Answer
from .forms import Qustion_form,Answer_form


def index(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            question = request.POST.get('question')
            posted_by = request.user
            q = Question(question_title=title, question_description=question, posted_by=posted_by)
            q.save()
            return redirect(index, q.qid, q.slug)
        except Exception as e:
            return render(request, 'qna/index.html', { 'error': 'Something is wrong with the form!' })
    else:
        context = {}
        context['questions'] = Question.objects.all()
        return render(request,'qna/index.html',context)

