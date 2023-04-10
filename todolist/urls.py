from django.urls import path
from .views import HomePageView, CreatePostView, DetailPostView, DetailToDoView, DeletePostView
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('contacts/', views.test, name='contacts'),
    # path('post/', views.post_v, name='post'),
    path('task/', views.task_v, name='task'),

    path('home/', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('detail/', DetailPostView.as_view(), name='detail'),
    path('detail1/', DetailToDoView.as_view(), name='detail_2'),
    path('delete/', DeletePostView.as_view(), name='delete_2'),


    path('more_button/', views.more_button, name='more_button'),


    path('delete/<int:todo_id>/', views.delete, name='delete'),


]
