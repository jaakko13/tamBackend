from rest_framework import serializers
from .models import Posts
from .models import Replies

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ["id", "title", "content", "createdAt", "author", "flair"]
        
class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ["id", "createdAt", "top_parent", "content", "author"]