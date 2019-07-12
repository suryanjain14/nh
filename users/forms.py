from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import profile


class user(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control needs-validation', 'placeholder': 'Enter email'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-inline form-control needs-validation ', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': ' form-inline form-control needs-validation', 'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-group form-control needs-validation needs-validation', 'placeholder': 'Username'}))
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput(
        attrs={'class': 'form-group form-control needs-validation', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput(
        attrs={'class': 'form-group form-control needs-validation', 'placeholder': 'Re-enter Password'}), )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', ]


class login(LoginView):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-group form-control needs-validation needs-validation', 'placeholder': 'Username'}))
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput(
        attrs={'class': 'form-group form-control needs-validation', 'placeholder': 'Enter Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class userupdateform(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control needs-validation', 'placeholder': 'Enter email'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-inline form-control needs-validation ', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': ' form-inline form-control needs-validation', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class profileupdateform(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(
        #    attrs={'class' : "btn btn-secondary", 'type': "button", 'placeholder': 'Choose image' }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control needs-validation'}))
    country = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control needs-validation'}))
    college = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control needs-validation'}))
    dob = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control form-control needs-validation'}))

    class Meta:
        model = profile
        fields = ['image', 'city', 'country', 'college', 'dob']
