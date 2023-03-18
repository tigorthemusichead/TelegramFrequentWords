from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('tutorial/', views.tutorial_page),
    path('uploadFile/', views.uploadFile)
]