from django.shortcuts import render
from django.contrib.auth.models import User


def cont(request):
    try:
        u_form = User.objects.get(username=request.user)

    except:
        u_form = None

    return render(request, "contact/index.html", {'u_form': u_form})
