from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category

class CategoryView(ViewSet):
    """This will serve as the view for Categories and handle ALL methods for server side"""

    def create(self, request):
        """Handle POST requests for categories"""

        new_category = Category()
        new_category.label = request.data['label']
        new_category.save()

        serialized = CategorySerializer(new_category)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        """Handles GET requests for all categories"""

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Single category request handler"""

        category = Category.objects.get(pk=pk)
        serialized = CategorySerializer(category)
        return Response(serialized.data, status=status.HTTP_200_OK)


class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories"""

    class Meta:
        model = Category
        fields = ('id', 'label')
