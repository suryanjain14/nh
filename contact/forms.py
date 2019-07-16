from .models import msg,msguser
from django.forms import ModelForm
from django import urls

class msg_form(ModelForm):
    class Meta:
        model=msg
        fields=['message']


class msguser_form(ModelForm):
    class Meta:
        model=msguser
        fields=['msgusername','email']