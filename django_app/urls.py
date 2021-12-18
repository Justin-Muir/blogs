from django.urls import path
from .views import *

urlpatterns= [
    path('post/new', BlogCreateview.as_view(), name= 'post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name= 'post'),
    path('update_post/<int:pk>/', UpdateBlog.as_view(), name = 'update_blog'),
    path('delete_blog/<int:pk>/delete/', DeleteBlog.as_view(), name = 'delete_blog'),
    path('', BlogListView.as_view(), name= 'home'),
]