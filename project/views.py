from django.shortcuts import render

# Create your views here.
def project(request):
    return render(request, 'project/project.html')
