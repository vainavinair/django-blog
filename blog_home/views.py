from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Posts

# Create your views here.

@login_required
def home(request):
    context = {
        'Posts' : Posts
    }
    return render(request,"blog_home/home.html",context=context)