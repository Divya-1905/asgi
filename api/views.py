
from ast import Delete
from cmath import log
import email
from lib2to3.pgen2 import token
from typing import Generic
from urllib import request
from venv import create
from webbrowser import get
from rest_framework.response import Response
from api.Serializer import signupserialiser, userserializers,todoserializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from api.models import user,Todo


class Signup(CreateAPIView):
    serializer_class =  signupserialiser
    queryset = user.objects.all()
    permission_classes = [AllowAny]

   
    def create(self, request):
        serializer = signupserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    
class loginview(APIView):
    serializer_class =  userserializers
    quertyset = user.objects.all()
    permission_classes = [AllowAny]
    def post(self,request):
        email = request.data.get('email')
        phone = request.data.get('phone')
        print(email,phone)
        
        try:
            User =  user.objects.get(email=email,phone=phone)
            print(User,'hai')
        except:
            return Response({"status":"dosenotexist"},status=status.HTTP_201_CREATED)
        if User:
            login(request,User)
            token,created = Token.objects.get_or_create(user=User)
            id = User.id
            data ={
                "token": token.key,
                "id":id}
                
            return Response({'status':'login','data':data},status=status.HTTP_200_OK)
        
class Logout(APIView):
    def get(self,request):
        logout(request)
        return Response({'status':'logout'})    
class EditUser(RetrieveUpdateDestroyAPIView):  
    queryset = user.objects.all()
    serializer_class =  userserializers
    permission_classes =[AllowAny]
    def update(self,request,pk):
        instance= user.objects.get(id=pk)
        print(instance)
        serializer = userserializers(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"update"},status=status.HTTP_200_OK)
        return Response({'error':serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)


class  CreateTodo(CreateAPIView)  : 
    serializer_class = todoserializer
    queryset = Todo.objects.all()
    permission_classes=[AllowAny]
    def  create(self,request):
        serializer = todoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status:created"},status=status.HTTP_200_OK)
        return Response({'status':serializer.errors},status=status.HTTP_204_NO_CONTENT)
    def get(self,request):
       User = request.user
       print(User)
       queryset = Todo.objects.filter(accountuser=User)
       print(queryset)
       serializer = todoserializer(queryset,many =True)
       return Response(serializer.data)
class UpdateTodo(RetrieveUpdateDestroyAPIView):  
    queryset = Todo.objects.all()
    serializer_class =   todoserializer
    permission_classes =[AllowAny]
    def update(self,request,pk):
        instance= Todo.objects.get(id=pk)
        serializer =  todoserializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"status":"update"},status=status.HTTP_200_OK)
        return Response({'error':serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)  








      
       




# class updatename2(RetrieveUpdateAPIView):
#     queryset = user.objects.all()
#     serializer_class= userserializers
#     permission_classes = [AllowAny]
#     def update(self,request,pk):
#         value = user.objects.get(id=pk)
#         serializer = userserializers(value,data=request.data)
#         if serializer.valid():
#             serializer.save()
#             return Response({"status":"update"},status=status.HTTP_200_OK)
#         return Response'({"error":"error "},status=status.HTTP_101_SWITCHING_PROTOCOLS) 
    
                
            
            
   
 
        
        
        
        
            
