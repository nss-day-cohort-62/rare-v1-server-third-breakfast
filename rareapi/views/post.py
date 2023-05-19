from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, RareUser, Category

class PostView(ViewSet):
    """Rare Post view"""

    def list(self, request):
        """Handle GET requests to get all posts

        Returns:
            Response -- JSON serialized list of posts
        """
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for single post

        Returns:
            Response -- JSON serialized post
        """
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

class PostRareUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RareUser
        fields =('id', 'full_name')

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'label')

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    user = PostRareUserSerializer(many=False)
    category = PostCategorySerializer(many=False)
    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved', 'post_tags', "post_reaction")
