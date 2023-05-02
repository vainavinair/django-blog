from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

from django.contrib.auth.models import User

from .models import Posts
from .forms import StudentModelForm

# Create your views here.

@login_required
def home(request):
    form = StudentModelForm(request.POST or None)
    if request.method=="GET":
        posts = Posts.objects.all()
        for post in posts:
            print(post.id)
        context = {
            'Posts' : posts,
            'form' : form
        }
        return render(request,"blog_home/home.html",context=context)
    elif request.method=="POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
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
    
def update_post(request,id):
    post = get_object_or_404(Posts, id=id)
    if request.user == post.author:
        if request.method=="POST":
            form = StudentModelForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('blog-home')

        else:
            form = StudentModelForm(instance=post)
        context = {'form': form}
        return render(request, "blog_home/update.html", context)
    else:
        return HttpResponseForbidden()

        