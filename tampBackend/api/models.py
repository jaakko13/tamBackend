from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, default='')
    flair = models.CharField(max_length=20, default='Discussion')
    
    def __str__(self):
        return self.title
    
class Replies(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    top_parent = models.IntegerField()
    content = models.TextField()
    author = models.CharField(max_length=50)
    
    

