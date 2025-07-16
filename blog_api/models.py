from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=50,
    )
    content = models.TextField()
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )


class Comment(models.Model):
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="comments_created",
    )
    posts = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
