from django.views.generic import ListView
from django.urls import path

from .views import (SearchProjectView,
                )

urlpatterns = [
    path('', SearchProjectView.as_view(), name='query'),
]