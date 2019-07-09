from . import views
from django.urls import path

urlpatterns = [

    path('groupdb/<pk>/', views.groupdb, name='groupdb'),
    path('gp/<pk>', views.groupprofile, name='groupprofile')
]
