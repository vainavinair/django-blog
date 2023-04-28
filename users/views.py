import uuid
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView

from user_profile.models import Profile
from .forms import UserRegisterForm

class CustomLoginView(LoginView):
    template_name = 'users/login.html'  # Use your own login template

    def form_valid(self, form):
        user = form.get_user()
        profile_obj = Profile.objects.filter(user=user).first()
        if  profile_obj.is_verified:
            return super().form_valid(form)
        messages.error(self.request, 'Your account is not verified yet.')
        return redirect('user-login')


def register(request):
    if request.method == 'POST':  
        form = UserRegisterForm(request.POST)  
        if form.is_valid():  
            email=form.cleaned_data.get('email')
            username=form.cleaned_data.get('username')
            user = form.save()
            token=str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user, auth_token=token)
            profile_obj.save()
            print(email,token)
            send_mail_otp(email,token)
            messages.success(request,f"Account created for {username}!")
            return redirect('user-token')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form}) 

def success(request):
    return render(request,'users/success.html')

def token_send(request):
    return render(request,'users/token.html')

def send_mail_otp(email,token):
    subject = "Email verification"
    message = f'Click this link to verify your account http://localhost:8000/user/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email=email_from, recipient_list=recipient_list)

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if not profile_obj.is_verified:
            profile_obj.is_verified=True
            profile_obj.save() 
            messages.success(request,f"Account has been verified. Welcome to our blog app {profile_obj.user.username}!")
            return redirect('user-login')
        else:
            messages.success(request,f"Account has been verified already")
            return redirect('user-login')

    except:
        return redirect('error-page')
    
def error_page(request):
    return render (request, 'error.html')