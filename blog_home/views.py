from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator, EmptyPage

from django.contrib.auth.models import User

from .models import Posts
from .forms import StudentModelForm

# Create your views here.

@login_required
def home(request):
    # Fetch all posts
    posts = Posts.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog_home/home.html', context=context)


def delete_post(request,id):
    # post = Posts.objects.filter(id=id).first()
    post = get_object_or_404(Posts, id=id)
    if request.user == post.author:
        post.delete()
        return redirect('blog-home')
    else: 
        messages.info(request,f"You dont have the persmission to delete this post")
        return redirect('blog-home')
    
@login_required
def create_post(request):
    form = StudentModelForm(request.POST or None)
    context = {
        'form':form
    }
    if request.method=="POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('blog-home')
    elif request.method=="GET":
        return render(request,"blog_home/create.html",context=context)

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

        