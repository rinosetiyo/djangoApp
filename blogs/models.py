from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.category_name
    
class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.tag_name

class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.username.first_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='categories')
    tags = models.ManyToManyField(Tag, null=True, blank=True, related_name='tags')
    views = models.IntegerField(default=0)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title