from django.shortcuts import render
from .models import Group
# Create your views here.

def groupdb(request, pk):
    group = Group.objects.get(pk=pk)
    arg = {'group': group}
    return render(request, 'groups/groupdb.html', arg)


def groupprofile(request, pk):
    group = Group.objects.get(pk=pk)
    arg = {'group': group}
    return render(request, 'groups/groupprofile.html', arg)
