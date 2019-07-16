from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import msg_form,msguser_form


def cont(request):
    try:
        i=1
        u_form = User.objects.get(username=request.user)
        p_form = msg_form(request.POST or None, request.FILES or None)


    except:
        i=2
        u_form = msguser_form(request.POST or None, request.FILES or None)
        p_form = msg_form(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if i==1:
            int2 = p_form.save(commit=False)
            from_email = [request.user.email]
        else:
            int1=u_form.save(commit=False)
            int2=p_form.save(commit=False)
            from_email = [int1.email]
        subject = 'Review to NerdHerd!'
        message = int2.message
        to_list = ['nerdherdindore@gmail.com']
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return redirect('home')

    return render(request, "contact/contact1.html",{'u_form':u_form,'p_form':p_form})
