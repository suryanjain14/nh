"""nh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage import views as hv
from users import views as uv
from django.contrib.auth import views as auth
from users.forms import login as l
from django.conf import settings
from django.conf.urls.static import static

#from  user import forms
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hv.h, name='home'),
    path('login/' , l.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('signup/', uv.register, name='signup'),
    path('profile/', uv.profile, name='profile'),
    path('profileup/', uv.profileupdate, name='profileup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
