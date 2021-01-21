from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post


# def home(request):
#     return HttpResponse("Hello World")

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'