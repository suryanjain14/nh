from django.shortcuts import render, redirect
from .models import Group
from .forms import groupedit
# Create your views here.

def groupdb(request, pk):
    group = Group.objects.get(pk=pk)
    arg = {'group': group}
    return render(request, 'groups/groupdb.html', arg)


def groupprofile(request, pk):
    group = Group.objects.get(pk=pk)

    # groups = Group.objects.all()
    # for group in groups:
    #    for user in group.users.all:
    #       if user == request.user:
    #          userd
    if request.method == 'POST':
        gform = groupedit(request.POST)  # ,request.user)
        if gform.is_valid():
            gform.save()

    else:
        gform = groupedit(request.POST)  #,request.user)

    arg = {'group': group, 'form': gform}
    return render(request, 'groups/groupprofile.html', arg)
