from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .exceptions import PostNotFoundError
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer


class PostViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        try:
            return Post.objects.get(pk=self.kwargs["pk"])
        except Post.DoesNotExist:
            raise PostNotFoundError


class CreatePostView(LoginRequiredMixin, ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CreateCommentView(LoginRequiredMixin, CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
