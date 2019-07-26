from django.shortcuts import render,redirect
from .models import Project,Userpro

# Create your views here.
def project(request):
    return render(request, 'Create_new_project_page/create_new_project.html')


def prostart(request, pk):
    new_project = Project.objects.get(pk=pk)
    Userpro.start_project(request.user, new_project)
    return  redirect('db')

'''
def friend(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
    return redirect('db')


'''