from django.forms import ModelForm
from QnA.models import Question,Answer


class Question_form(ModelForm):
    class Meta:
        model=Question
        fields=['question_title','question_description','posted_by']


class Answer_form(ModelForm):
    class Meta:
        models=Answer
        fields=['answer_description']