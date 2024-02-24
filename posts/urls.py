from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.posts_index, name='index'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('create/', views.post_create, name='create'),
    path('chat/', views.chat, name='chat'),

]