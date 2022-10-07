from unicodedata import name
from django.urls import path
from .views import *
urlpatterns = [
    path('signup', signup.as_view(),name='user'),
    path('Login',loginview.as_view(),name='login'),
    path('update/<str:pk>',updatename.as_view(),name='update'),
   
    path('indexlogin/',   index.as_view(),name='todologin'),
    path('updatetodo/<str:pk>', update1.as_view(),name='update'),
    path('logout', logouttodo.as_view(),name='logout'),
   
   
] 