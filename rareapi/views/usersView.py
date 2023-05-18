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

    # def retrieve(self, request, pk=None):
    #     """Handle GET requests for single game

    #     Returns:
    #         Response -- JSON serialized game
    #     """
    #     try:
    #         gamer = Gamer.objects.get(pk=pk)
    #         serializer = GamerSerializer(gamer)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Gamer.DoesNotExist as ex:
    #         return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


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


# class CreateGamerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gamer
#         fields = [
#             "id",
#             "user",
#             "bio",
#         ]
