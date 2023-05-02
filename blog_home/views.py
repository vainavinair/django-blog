from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

from django.contrib.auth.models import User

from .models import Posts

# Create your views here.

@login_required
def home(request):
    if request.method=="GET":
        posts = Posts.objects.all()
        for post in posts:
            print(post.id)
        context = {
            'Posts' : posts
        }
        return render(request,"blog_home/home.html",context=context)
    elif request.method=="POST":
        author = User.objects.filter(username=request.user).first()
        title = request.POST.get('post-title')
        content = request.POST.get('post-content')
        post = Posts(author=author, title=title, content=content)
        post.save()
        return redirect('blog-home')


def delete_post(request,id):
    # post = Posts.objects.filter(id=id).first()
    post = get_object_or_404(Posts, id=id)
    if request.user == post.author:
        post.delete()
        return redirect('blog-home')
    else: 
        messages.info(request,f"You dont have the persmission to delete this post")
        return redirect('blog-home')
    
def update_post(request, id):
    post = get_object_or_404(Posts, id=id)
    if request.user == post.author:
        if request.method == "POST":
            title = request.POST.get('post-title')
            content = request.POST.get('post-content')
            post.title = title
            post.content = content
            post.save()
            return redirect('blog-home')
        else:
            context = {'post': post}
            return render(request, 'blog_home/update.html', context)
    else: 
        messages.info(request,f"You dont have the persmission to update this post")
        return redirect('blog-home')

        