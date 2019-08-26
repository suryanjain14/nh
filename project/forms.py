from django.forms import ModelForm
from .models import Project1

class Project1(ModelForm):
    class Meta:
        models=Project1
        fields=['pro_name','prerequisite','description','duration']
