"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import RareUser
from django.contrib.auth.models import User


class RareUsersView(ViewSet):
    """Rare all users view"""

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """

        rare_users = RareUser.objects.all()

        serializer = RareUserSerializer(rare_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single user detail

        Returns:
            Response -- JSON serialized user
        """
        try:
            user = RareUser.objects.get(pk=pk)
            serializer = RareUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RareUser.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "date_joined", "username", "first_name", "last_name")


class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for rare users"""

    user = UserSerializer(serializers.ModelSerializer)

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
