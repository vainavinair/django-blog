from django.urls import path
from .views import home, delete_post, update_post,create_post
 
urlpatterns = [
    path('', home , name='blog-home'),     
    path('post/delete/<id>', delete_post , name='post-delete'),     
    path('post/update/<id>', update_post , name='post-update'),     
    path('post/create/', create_post , name='post-create'),     
]