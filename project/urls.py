from . import views
from django.urls import path


urlpatterns = [

    path('new/', views.project, name='project'),
    path('exp/', views.project, name='exp'),


]
