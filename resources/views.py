from django.shortcuts import render
from .models import *
from .forms import Imagefor
# Create your views here.


def resource(request):
    lang = Language.objects.all()
    files = Resofile.objects.all()
    img = Resoimg.objects.all()
    link = Reslink.objects.all()
    Ftag = Resource_Platform_file.objects.all()
    Itag = Resource_Platform_img.objects.all()
    Ltag = Resource_Platform_link.objects.all()
    args = {'lang': lang, 'files': files, 'img': img, 'link': link, 'Ftag': Ftag, 'Ltag': Ltag, 'Itag': Itag}
    return render(request, 'resource/index.html', args)


def addimg(request):
    form = Imagefor(request.POST)
    user = request.user
    arg = {'form': form}

    return render(request, 'resource/addl.html', arg)
