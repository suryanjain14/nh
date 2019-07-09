from django import forms
from django.urls import path
from . import views

urlpatterns = [
 path('',views.cont,name='contact'),

]
