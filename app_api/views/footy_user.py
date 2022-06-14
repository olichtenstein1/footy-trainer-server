"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from app_api.models import FootyUser


class FootyUserView(ViewSet):
    
    def retrieve(self, request, pk):
        
        footy_user = FootyUser.objects.get(pk=pk)
        serializer = FootyUserSerializer(footy_user)
        return Response(serializer.data)

    def list(self, request):
        
        footy_users = FootyUser.objects.all()
        serializer = FootyUserSerializer(footy_users, many=True)
        return Response(serializer.data)

        
class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email' )
        

class FootyUserSerializer(serializers.ModelSerializer):
   
    user = UserSerializer()
    class Meta:
        model = FootyUser
        fields = ('id', 'bio', 'profile_picture', 'user', 'favorite_player', 'favorite_player_img', 'years_of_experience' )
        depth = 2