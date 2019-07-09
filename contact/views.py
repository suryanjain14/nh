from django.shortcuts import render

def cont(request):
    return render(request,"contact/index.html",{})
