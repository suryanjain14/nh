from django.forms import ModelForm
from QnA.models import Question,Answer


class Qustion_form(ModelForm):
    class Meta:
        models=Question
        fields=['question_title','question_description']


class Answer_form(ModelForm):
    class Meta:
        models=Answer
        fields=['answer_description']