
from django.http import HttpResponse

from .models import *
from django.shortcuts import render,redirect
from .forms import loginform, signupform,todosignupform,todoupdateform
# from api import form 


def signup(request):
    form = signupform()
    
    return render(request,'api/signup.html',{'form':form})
def login(request):
    form = loginform()
    return render(request,'api/login.html',{'form':form})
def createtodo(request):
    form = todosignupform()
    form2 = todoupdateform()
    return render (request,'api/todo.html',{'form':form})
def updatetodo(request):
    form = todoupdateform()
    return render(request,'api/updatetodo.html',{'form':form})
def index(request):
    form = loginform()
    return render(request,'api/index.html',{'form':form})