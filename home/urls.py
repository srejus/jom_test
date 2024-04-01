from django.urls import path
from .views import *

urlpatterns = [
    path('home',IndexView.as_view()),
]