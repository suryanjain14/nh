from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project, Userpro, Project1
from django.http import Http404

# Create your views here.

'''
class ProjectListView(ListView):
    
    template_name = "project/project1.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return project1.objects.all()
'''

class ProjectListView(ListView):
    # queryset = Project.objects.all()
    template_name = "project/project1.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Project.objects.all()

# def project(request):
#     queryset = project1.objects.all().order_by('created_on')
#     context ={
#         "object_list": queryset
#     }
#     return render(request, 'project/project1.html', context)

def project(request):
    pro=Project1.objects.all().order_by('created_on')
    return render(request, 'project/project1.html',{'pro':pro})

def custom(request):
    return render(request, 'create_new_project_page/create_new_project.html')

def prostart(request, pk):
    new_project = Project.objects.get(pk=pk)
    Userpro.start_project(request.user, new_project)
    return redirect('db')


def explore(request, pk):
    pro = Project1.objects.get(pk=pk)
    arg = {'pro': pro}
    return render(request, 'project/exploreproject.html', arg)


'''
def friend(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
    return redirect('db')
'''