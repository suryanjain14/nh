from django.forms import ModelForm
from .models import project1

class project(ModelForm):
    class Meta:
        models=project1
        fields=['pro_name','prerequisite','description']
