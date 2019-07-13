from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from nh import settings
from django.contrib import messages

def cont(request):
    try:
        u_form = User.objects.get(username=request.user)


    except:
        u_form = None

    if request.method == "POST":


            subject = 'Thankyou for registering on NerdHerd!!'
            message = 'this is messages'
            from_email = [u_form.email]
            to_list = ['nerdherdindore@gmail.com']
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            return redirect('home')

    return render(request, "contact/index.html", {'u_form': u_form})
