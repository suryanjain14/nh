from django import forms
from django.forms import ModelForm
from .models import Resoimg


class Image(ModelForm):
    name = forms.CharField()
    image = forms.ImageField()
    description = forms.CharField()
    language = forms.ChoiceField(widget=forms.Select, choices=(
    ("Python", "Python"), ("Java", "Java"), ("CFamily", "CFamily"), ("JavaScript", "JavaScript"),))

    class Meta:
        model = Resoimg
        fields = ['name', 'image', 'language', 'description']
