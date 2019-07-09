from django.contrib import admin
from django.urls import path, include
from homepage import views as hv
from users import views as uv
from django.contrib.auth import views as auth
from users.forms import login
from django.conf import settings
from django.conf.urls.static import static
from project import views as pv
from news_update import urls
from mtteam import views as mtt


# from  user import forms
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hv.h, name='home'),
    path('login/', login.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('signup/', uv.register, name='signup'),
    path('profile/', uv.profile, name='profile'),
    path('profileup/', uv.profileupdate, name='profileup'),
    path('password-reset/', auth.PasswordResetView.as_view(template_name='user/password_reset.html'),
         name='password_reset'),
    path('password-reset-done/', auth.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'
         ),
    path('db/', uv.db, name='db'),
    path('profile/<pk>/', uv.profile_with_pk, name='view_profile'),
    path('connect/<operation>/<pk>/', uv.friend, name='friends'),
    path('db/add/', uv.add, name='add'),
    path('db/remove/', uv.remove, name='remove'),
    path('event/', include('news_update.urls'), name='event'),
    path('project/', pv.project),
    path('db/start/<pk>/starting', pv.prostart, name='startproject'),
    path('abt/', mtt.meet, name='mtt'),
    path('', include('groups.urls')),
    path('contact us/',include('contact.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
