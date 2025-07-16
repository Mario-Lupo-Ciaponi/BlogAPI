from rest_framework.serializers import ModelSerializer

from accounts.serializers import UserSerializer
from .models import Post, Comment


class CommentSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["author", "posts", "content", "created_at",]


class PostSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
