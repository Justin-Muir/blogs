from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, DetailView

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'blog_name'

class BlogDetailView(DetailView):
    model = Post
    # template_name = 'post_detail.html'
    context_object_name = 'Post_detail'
    