from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostsListCreate.as_view(), name="post-view-create"),
    path("replies/", views.RepliesListCreate.as_view(), name="reply-view-create")
]
