from django.shortcuts import render


# Create your views here.

def meet(request):
    return render(request, template_name='mtteam/index.html')
