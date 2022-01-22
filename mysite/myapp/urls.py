from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index2/', views.index2, name="index2"),
    path('index3/', views.index3, name="index3"),
    path('posts/', views.displayPosts, name="posts"),
    path('user/<int:id>', views.getUserById, name="getUser")
]
