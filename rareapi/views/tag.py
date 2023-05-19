from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Tag

class TagView(ViewSet):
    """Tag View"""
    def retrieve(self, request, pk): 
        """Handles GET requests for single tag 
        
        Returns: 
            Response --- JSON serialized tag
        """

        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
    
    def list(self, request): 
        """Handles GET requests for all tags
        
        Returns: 
            Response --- JSON serialized tags list
        """

        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def create(self, request): 
        """Handle POST operations 
        Returns 
            Response -- JSON serialized tag instance
        """
        new_tag = Tag()
        new_tag.label = request.data['label']
        new_tag.save()

        serialized = TagSerializer(new_tag)

        return Response(serialized.data, status=status.HTTP_201_CREATED)


class TagSerializer(serializers.ModelSerializer): 
    """JSON serializer for tags"""

    class Meta: 
        model = Tag
        fields = ('label', 'id')
        