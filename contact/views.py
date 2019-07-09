from django.shortcuts import render
from django.contrib.auth.models import User
def cont(request):
    u_form=User.objects.get(username=request.user)
    return render(request,"contact/index.html",{'u_form':u_form})
