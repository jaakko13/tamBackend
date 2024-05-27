from rest_framework import generics
#generics above
from .models import Posts
from .serializers import PostSerializer
from .models import Replies
from .serializers import RepliesSerializer
# Create your views here.

class PostsListCreate(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    
class RepliesListCreate(generics.ListCreateAPIView):
    queryset = Replies.objects.all()
    serializer_class = RepliesSerializer