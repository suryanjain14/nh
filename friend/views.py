from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from nh import settings
from django.contrib.auth.models import User


@login_required()
def db(request):
    users = User.objects.all().order_by('username')
    arg = {'users':users}
    return render(request, 'user/db.html', arg)

def profile_with_pk(request):
    return render(request, 'user/profile.html')
#kuch bhi