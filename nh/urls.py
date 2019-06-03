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
from users.forms import login
from django.conf import settings
from django.conf.urls.static import static

# from  user import forms
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hv.h, name='home'),
    path('login/', login.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('signup/', uv.register, name='signup'),
    path('profile/', uv.profile, name='profile'),
    path('profileup/', uv.profileupdate, name='profileup'),
    path('password-reset/', auth.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password-reset-done/', auth.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'
         ),
    path('db/', uv.db, name='db'),
    path(r'^profile/(?P<pk>\d+)/$', uv.profile_with_pk, name='view_profile'),
    path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', uv.friend, name='friends'),
    path('db/add/', uv.add, name='add'),
    path('db/remove/', uv.remove, name='remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
