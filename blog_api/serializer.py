from rest_framework.serializers import ModelSerializer

from accounts.serializers import UserSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
