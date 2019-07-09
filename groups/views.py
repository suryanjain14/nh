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
    pk = pk

    if request.method == 'POST':
        gform = groupedit(request.POST, pk)
        if gform.is_valid():
            gform.save()
            return redirect('groupprofile')
    else:
        gform = groupedit(request.POST, instance=request.user)

    arg = {'group': group, 'form': gform}
    return render(request, 'groups/groupprofile.html', arg)
