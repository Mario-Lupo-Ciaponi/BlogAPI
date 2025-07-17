from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .exceptions import PostNotFoundError
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer
from .permisions import IsAuthor


class PostViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthor | IsAdminUser]

    def get_object(self):
        try:
            return Post.objects.get(pk=self.kwargs["pk"])
        except Post.DoesNotExist:
            raise PostNotFoundError

    def check_permissions(self, request: HttpRequest):
        if request.method in ["DELETE", "PUT", "PATCH"]:
            for permission in self.get_permissions():
                if not permission.has_permission(request, self):
                    self.permission_denied(request, message="Permission denied")
        else:
            super().check_permissions(request)



class CreatePostView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CreateCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
