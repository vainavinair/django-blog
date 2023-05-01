from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Posts

# Create your views here.

@login_required
def home(request):
    posts = Posts.objects.all()
    context = {
        'Posts' : posts
    }
    print(context)
    return render(request,"blog_home/home.html",context=context)