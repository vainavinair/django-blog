from django.urls import path
from .views import home, delete_post
 
urlpatterns = [
    path('', home , name='blog-home'),     
    path('post/delete/<id>', delete_post , name='post-delete'),     
    path('post/update/<id>', home , name='post-update'),     
]