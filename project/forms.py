from django.forms import ModelForm
from .models import Project1

class Project1form(ModelForm):
    class Meta:
        model=Project1
        fields=['pro_name','prerequisite','description','duration','created_by']
