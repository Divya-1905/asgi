from django.urls import path
from .frontendview import *
urlpatterns=[
    path('signup',signup),
    path('login',login),
    path('todocreate',createtodo),
    path('updatetodo',updatetodo),
    path('',index)
]