import uuid
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from user_profile.models import Profile
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':  
        form = UserRegisterForm(request.POST)  
        if form.is_valid():  
            username=form.cleaned_data.get('username')
            user = form.save()
            profile_obj = Profile.objects.create(user=user, auth_token=str(uuid.uuid4()))
            profile_obj.save()
            # messages.success(request,f"Account created for {username}!")
            return redirect('user-token')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form}) 

def success(request):
    return render(request,'users/success.html')

def token_send(request):
    return render(request,'users/token.html')

def send_mail(email,token):
    subject = "Email verification"
    message = f'Click this link to verify your account http://localhost:8000/user/verify/{token}'
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_form, recipient_list )