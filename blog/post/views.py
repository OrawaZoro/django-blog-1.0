from django.shortcuts import render
from .models import BlogPost


def homePage(request):
    posts = BlogPost.objects.order_by('post_created')[:5]
    context = {'posts': posts}
    return render(request, 'post/home.html', context)


def post(request, pk):
    posts = BlogPost.objects.order_by('-post_created')[:3]
    selected_post = BlogPost.objects.get(pk=pk)
    context = {'selected_post': selected_post, 'posts': posts}
    return render(request, 'post/post.html', context)

def blog(request):
    blogs = BlogPost.objects.order_by('-post_created')[:20]
    context = {'blogs': blogs}
    return render(request, 'post/blogs.html', context)

def contact(request):
    return render(request, 'post/contact.html', {})