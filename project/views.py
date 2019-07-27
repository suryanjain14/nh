from django.shortcuts import render,redirect
from .models import Project,Userpro,project1

# Create your views here.
def project(request):
    pro=project1.objects.all().order_by('created_on')
    return render(request, 'project/project1.html',{'pro':pro})

def custom(request):
    return render(request, 'create_new_project_page/create_new_project.html')

def prostart(request, pk):
    new_project = Project.objects.get(pk=pk)
    Userpro.start_project(request.user, new_project)
    return redirect('db')


def explore(request, pk):
    pro = project1.objects.get(pk=pk)
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