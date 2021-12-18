from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "django_app/home.html"
    context_object_name = 'blog_name'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'django_app/blog_detail.html'
    context_object_name = 'Post_detail'
    
class BlogCreateview(CreateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = "django_app/create_blog.html"
    success_url = reverse_lazy ('home')

class UpdateBlog(UpdateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = "django_app/Update_blog.html"
    success_url = reverse_lazy('home')
    context_object_name = 'blog'

class DeleteBlog(DeleteView):
    model = Post
    template_name = 'django_app/delete_blog.html'
    success_url = reverse_lazy('home')