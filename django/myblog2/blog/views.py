from django.shortcuts import render

# Create your views here.
from .models import Post
from .models import PostCategory

def home(request):
    post_category = PostCategory.objects.all()
    return render(request, 'home.html', {
        'post_category': post_category
    })


def posts(request):
    post_category = PostCategory.objects.all()
    posts_lists = Post.objects.all()
    return render(request, 'posts.html', {
        'posts_lists': posts_lists,
        'post_category': post_category
    })


def post_one(request, post_id):
    post_category = PostCategory.objects.all()
    post = Post.objects.filter(id=post_id)
    return render(request, 'post_one.html', {
        'post': post.first(), 
        'post_category': post_category
    })

def post_cat(request, category_id):
    post_category = PostCategory.objects.all()
    posts_lists = Post.objects.filter(post_category_id = category_id)
    return render(request, 'posts.html', {
        'posts_lists': posts_lists,
        'post_category': post_category
    })