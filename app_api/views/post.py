"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Post, Category, FootyUser
from rest_framework.decorators import action

class PostView(ViewSet):
    

    def retrieve(self, request, pk):
        """Handle GET requests for single post"""
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
            
            """Returns:
                Response -- JSON serialized post
            """
        
        

    def list(self, request):
        """Handle GET requests to get all posts"""
        
        posts = Post.objects.all()
    
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

        """Returns:
            Response -- JSON serialized list of posts
        """
    
    def create(self, request):
       
        """Handle POST operations

        Returns:
            Response -- JSON serialized post instance
        """
        footy_user = FootyUser.objects.get(user=request.auth.user)
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(footy_user=footy_user)
        post = Post.objects.get(pk=serializer.data["id"])
        post.category.add(request.data["category"])
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    @action(methods=["get"], detail=False)
    def post_by_category(self, request):
        category = Category.objects.get(pk=request.query_params.get("category"))
        # use .order_by() eventually
        posts = Post.objects.filter(category=category)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Post
        fields = ('id','difficulty_level', 'description', 'video_tutorial', 'footy_user', 'topic', 'title', 'category')
        depth = 2
        
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'difficulty_level', 'description', 'video_tutorial', 'topic', 'title']