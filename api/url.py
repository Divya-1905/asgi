from unicodedata import name
from django.urls import path
from .views import *
urlpatterns = [
    path('signup', Signup.as_view(),name='user'),
    path('Login',loginview.as_view(),name='login'),
    path('update/<str:pk>',EditUser.as_view(),name='update'),
    path('createtodo/',   CreateTodo.as_view(),name='todologin'),
    path('updatetodo/<str:pk>', UpdateTodo.as_view(),name='update'),
    path('logout', Logout.as_view(),name='logout'),
] 