from django.shortcuts import render, get_object_or_404
from blogs.models import Post, Category, Comment
from blogs.forms import CommentForm

# Create your views here.
def index(request):
    popular = Post.objects.all().order_by('-views')[0:5]
    hero = Post.objects.all().order_by('-created_at')[0:4]
    post_entry_lg = Post.objects.all().order_by('-created_at')[0:1]
    post_entry_1 = Post.objects.all().order_by('-created_at')[1:4]
    post_entry_2 = Post.objects.all().order_by('-created_at')[4:7]
    categories = Category.objects.all()
    
    context = {
        'popular':popular,
        'hero':hero,
        'post_entry_lg':post_entry_lg,
        'post_entry_1':post_entry_1,
        'post_entry_2':post_entry_2,
        'categories':categories,
    }
    return render(request, 'index.html', context)

def single_post(request, id):
    popular = Post.objects.all().order_by('-views')[0:5]
    latest = Post.objects.all().order_by('-created_at')[0:5]
    hero = Post.objects.all().order_by('-created_at')[0:4]
    categories = Category.objects.all()

    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    comment_count = comments.count()
    post.views += 1
    post.save()

    form = CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            post_id = request.POST['post_id']
            comment.post = Post.objects.get(id=post_id)
            comment.message = request.POST['message']
            comment.save()

    context = {
        'popular':popular,
        'latest':latest,
        'hero':hero,
        'categories':categories,
        'post':post,
        'comments':comments,
        'comment_count':comment_count,
        'form':form,
    }
    return render(request, 'single-post.html', context)