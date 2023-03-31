from django.urls import path
from . import views

urlpatterns = [
    # views
    path('', views.home_page),
    path('tutorial/', views.tutorial_page),
    path('preview/<str:file_name>', views.preview_page),
    # api
    path('uploadFile/', views.uploadFile),
    path('contact/', views.contact),
    path('delete/', views.delete)
]