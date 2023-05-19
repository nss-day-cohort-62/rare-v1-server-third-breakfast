"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import RareUser


class UsersView(ViewSet):
    """Rare all users view"""

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """

        rare_users = RareUser.objects.all()

        serializer = RareUserSerializer(rare_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for rare users"""

    class Meta:
        model = RareUser
        fields = (
            "id",
            "bio",
            "profile_image_url",
            "created_on",
            "active",
            "user",
        )
        depth = 1
