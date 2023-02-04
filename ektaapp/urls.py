from django.urls import path, include
from .views import *
urlpatterns = [
    path("",LoginView.as_view(),name="login"),
    path("home/",HomeView.as_view(),name="home"),
]

