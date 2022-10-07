from dataclasses import fields
import email
from pyexpat import model
from django import forms
from api.models import user, Todo 

class signupform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confrim_password= forms.ChoiceField(widget=forms.PasswordInput())
    phone  = forms.CharField(max_length=10)
    

class loginform(forms.ModelForm):
    class Meta:
        model= user
        fields=['email','phone']       
        
class todosignupform(forms.ModelForm):
    class Meta:
        model =  Todo 
        fields = '__all__' 
        exclude=['accountuser']  
class todoupdateform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'       
        