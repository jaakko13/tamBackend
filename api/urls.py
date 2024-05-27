from django.urls import path
# from .views import *
from . import views


urlpatterns = [
    path("posts/", views.PostsListCreate.as_view(), name="post-view-create"),
    path("replies/", views.RepliesListCreate.as_view(), name="reply-view-create")

]

# router = DefaultRouter()
# router.register('posts', PostsListCreate, basename='posts')
# router.register('replies', RepliesListCreate, basename='replies')
# urlpatterns = router.urls