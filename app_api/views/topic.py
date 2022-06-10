from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Topic

class TopicView(ViewSet):
    
    def list(self, request):
        """Handle GET requests to get all topics"""
        
        topics = Topic.objects.all()
    
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

        """Returns:
            Response -- JSON serialized list of topics
        """
        
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id','label')
    