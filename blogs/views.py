from django.shortcuts import render, get_object_or_404
from blogs.models import Post, Category

# Create your views here.
def index(request):
    hero = Post.objects.all().order_by('-created_at')[0:4]
    post_entry_lg = Post.objects.all().order_by('-created_at')[0:1]
    post_entry_1 = Post.objects.all().order_by('-created_at')[1:4]
    post_entry_2 = Post.objects.all().order_by('-created_at')[4:7]
    categories = Category.objects.all()
    
    context = {
        'hero':hero,
        'post_entry_lg':post_entry_lg,
        'post_entry_1':post_entry_1,
        'post_entry_2':post_entry_2,
        'categories':categories,
    }
    return render(request, 'index.html', context)

def single_post(request, id):
    hero = Post.objects.all().order_by('-created_at')[0:4]
    categories = Category.objects.all()
    
    post = get_object_or_404(Post, id=id)

    context = {
        'hero':hero,
        'categories':categories,
        'post':post,
    }
    return render(request, 'single-post.html', context)