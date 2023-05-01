from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile


def profile(request,username):
    user = User.objects.filter(username=username).first()
    user_profile = Profile.objects.filter(user=user).first()
    context = {'profile':user_profile}
    return render(request,'user_profile/profile.html',context)