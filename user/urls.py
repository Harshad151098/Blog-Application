from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('register/',views.register,name='user-register'),
    path('profile/',views.profile,name='user-profile'),
    path('',views.home,name='user-home'),

]
