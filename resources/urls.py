from . import views
from django.urls import path

urlpatterns = [

     path('re', views.resource, name='resource'),
     path('add', views.addimg, name='Aimg'),


]
