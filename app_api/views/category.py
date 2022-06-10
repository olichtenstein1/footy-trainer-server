"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Category

class CategoryView(ViewSet):
    

    def retrieve(self, request, pk):
        """Handle GET requests for single category"""
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
            
            """Returns:
                Response -- JSON serialized category
            """
        
        

    def list(self, request):
        """Handle GET requests to get all game types"""
        
        categories = Category.objects.all()
    
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

        """Returns:
            Response -- JSON serialized list of categories
        """

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Category
        fields = ('id', 'label')