from django.urls import path, include
from . import views

urlpatterns = [
    path("post/", include([
        path("", views.CreatePostView.as_view(), name="create-post"),
        path("<int:pk>/", views.PostViewSet.as_view(), name="post-viewset"),
    ])),
    path("comment/", views.CreateCommentView.as_view(), name="create-comment"),
]