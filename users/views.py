from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from.forms import user,userupdateform,profileupdateform #,login
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):

    if request.method == "POST":
        form = user(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username} Account created!')
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
    return render(request,'user/profile.html')

@login_required
def profileupdate(request):
    if request.method== 'POST':
        u_form = userupdateform(request.POST,instance=request.user)
        p_form = profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        u_form.save()
        p_form.save()
        messages.success(request, f'Profile Saved')
        return redirect('profile')

    else:
        u_form = userupdateform(request.POST,instance=request.user)
        p_form = profileupdateform(request.POST,instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'user/profileupdate.html',context)