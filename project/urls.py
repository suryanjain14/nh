from . import views
from django.urls import path


urlpatterns = [

    path('new/', views.project, name='project'),
    path('exp/<pk>', views.explore, name='exp'),
    path('custom project/', views.proview, name='custom'),


]
