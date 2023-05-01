from django.urls import path
from .views import register, token_send, success, verify, error_page, CustomLoginView
from django.contrib.auth import views as auth_views

from user_profile import views as profile_views


urlpatterns = [
    path('register/',register, name='user-register'),
    path('login/',CustomLoginView.as_view(), name='user-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),
    path('token/',token_send, name='user-token'),
    path('success/',success, name='user-success'),
    path('verify/<auth_token>',verify, name='verify'),
    path('error/',error_page, name='error-page'),
     path('profile/<username>/', profile_views.profile, name='user-profile'),
]
