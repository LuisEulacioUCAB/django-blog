from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name = "home"),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name = "post-delete"),
    path('create/', views.CreatePost.as_view(), name = "post-create"),
    path('update/<int:pk>/', views.UpdatePost.as_view(), name = "post-update"),
    path('details/<int:pk>/', views.DetailPost.as_view(), name = "post-detail"),
    path('comment/', views.create_comment, name = "create-comment"),

]

