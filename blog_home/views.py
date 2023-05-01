from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Posts

# Create your views here.

@login_required
def home(request):
    if request.method=="GET":
        posts = Posts.objects.all()
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
    post = Posts.objects.filter(id=id).first()
    post.delete()
    return redirect('blog-home')
    