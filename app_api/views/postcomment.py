from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from app_api.models import Comment
from app_api.models.footyuser import FootyUser


class CommentView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single post comment"""
        
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
        
        
    def list(self, request):
        """Handle GET requests to get all post comments"""
        
        comments = Comment.objects.all()
        
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        
        """Handle POST operations

        Returns:
            Response -- JSON serialized post comment instance
        """
        footy_user = FootyUser.objects.get(user=request.auth.user)
        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(footy_user=footy_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for post comments
    """
    class Meta:
        model = Comment
        fields = ('id', 'content', 'rating', 'footy_user', 'post')
        depth = 3     
        
class CreateCommentSerializer(serializers.ModelSerializer):
    """JSON serializer for creating post comments
    """
    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'rating')