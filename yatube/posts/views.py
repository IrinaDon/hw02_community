from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    POSTS_PER_PAGE = 10
    # posts = Post.objects.order_by('-pub_date')[:10]
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    POSTS_PER_PAGE = 10
    # posts = Post.objects.filter(group=group).order_by('-pub_date')
    # [:POSTS_PER_PAGE]
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'group_list.html', context)
