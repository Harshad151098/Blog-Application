from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListview,PostDetailview,PostCreateview,PostUpdateView,PostDeleteview,UserListview

urlpatterns = [
    path('', PostListview.as_view(),name='blog-home'),
    path('user/<str:username>', UserListview.as_view(),name='user-posts'),
    path('post/<int:pk>', PostDetailview.as_view(),name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteview.as_view(),name='post-delete'),
    path('post/new/', PostCreateview.as_view(),name='post-create'),
    path('about/', views.about,name='blog-about'),
]
