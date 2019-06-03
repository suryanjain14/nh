from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from.forms import user,userupdateform, profileupdateform #,login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from nh import settings
from django.contrib.auth.models import User
from . models import Friend


# Create your views here.
def register(request):

    if request.method == "POST":
        form = user(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            subject='Thankyou for registering on NerdHerd!!'
            message='Welcome to NerdHerd,We very much appreciate your response'
            from_email=settings.EMAIL_HOST_USER
            to_list=[email]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            messages.success(request, f'{username} Account created!')
            return redirect('home')
    else:
        form = user

    return render(request,'user/reg.html',{'form':form})


"""def login(request):
    if request.method == "POST":
        form = login(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username} LoggedIN')
            return redirect('home')
    else:
        form = login

    return render(request,'user/login.html',{'form':form})
"""
@login_required
def profile(request):
    return render(request, 'user/profile.html')


@login_required
def profileupdate(request):
    if request.method == 'POST':
        u_form = userupdateform(request.POST, instance=request.user)
        p_form = profileupdateform(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Saved')
            return redirect('profile')

    else:
        u_form = userupdateform(request.POST, instance=request.user)
        p_form = profileupdateform(request.POST, instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/profileupdate.html',context)


@login_required()
def db(request):
    users = User.objects.all().order_by('username')
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()
    arg = {'users': users, 'friends': friends}
    return render(request, 'user/db.html', arg)


def profile_with_pk(request,pk):

    user = User.objects.get(pk=pk)
    arg = {'user': user}
    return render(request, 'user/profile.html', arg)


def friend(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
    return render(request, 'user/db.html')


def add(request):
    users = User.objects.all().order_by('username')
    arg = {'users': users}
    return render(request, 'user/add.html',arg)


def remove(request):
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()
    arg = {'friends': friends}
    return render(request, 'user/remove.html', arg)