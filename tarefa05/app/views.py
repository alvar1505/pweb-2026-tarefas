from django.shortcuts import render, get_object_or_404 
from .models import Post

def index(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "app/index.html", context) 

def post(request, post_id):
    context = {
        "post": get_object_or_404(Post, id=post_id),
    }
    return render(request, "app/posts.html", context)