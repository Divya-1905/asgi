from dataclasses import field, fields
import email
from rest_framework import serializers
from api.models import user,Todo

class userserializers(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['email','phone']
class signupserialiser(serializers.ModelSerializer)  :
    class Meta:
        model = user 
        fields = [ 'email','phone','password'] 
    def create(self, validated_data):
          user1 = user.objects.create(
              email=validated_data['email'],
              phone=validated_data['phone'],
            
            )
          user1.set_password(raw_password=validated_data['password']) 
          user1.save()
          return user1
class todoserializer(serializers.ModelSerializer):
    accountuser = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        fields = ['id','accountuser','tittle','details','notification','complete','takenHours','plannedhours']
          