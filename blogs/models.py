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
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='categories')
    tags = models.ManyToManyField(Tag, null=True, blank=True, related_name='tags')
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message