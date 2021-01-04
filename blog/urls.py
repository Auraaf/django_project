from django.urls import path
from . import views
urlpatterns = [
    #calling from django_project.urls empty string ''
    path('', views.home , name= 'blog-home'),
    #2 (look 1 in urls) now it will try to find empty string corresponding to that it will return addres i.e views.home.
    #navigate to views.home function.
    path('about/', views.about , name= 'blog-about'),
]