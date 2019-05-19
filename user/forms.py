from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm

class user(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name =forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    username= forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2',]

class login(AuthenticationForm):
    username = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))