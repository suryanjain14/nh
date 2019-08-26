from django import forms
from django.forms import ModelForm
from .models import Resoimg


class Imagefor(ModelForm):
    name = forms.CharField()
    image = forms.ImageField()
    description = forms.CharField()
    language = forms.ChoiceField(widget=forms.Select, choices=(
    ("Python", "Python"), ("Java", "Java"), ("CFamily", "CFamily"), ("JavaScript", "JavaScript"),))

    class Meta:
        model = Resoimg
        fields = ['name', 'image', 'language', 'description']
        exclude = ('time', 'creator', 'promoter',)


'''
        def __init__(self,user, *args, **kwargs):
            self.user = user
            super(Imagefor, self).__init__(*args, **kwargs)

        def save(self):
            image = super(Imagefor, self).save(commit=False)
            image.user = self.user
            image.save()
            return image

'''
