from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Main, name = 'Main'),
    path('result/', views.Result, name = 'Result'),
    path('about/', views.About, name = 'About'),
]
