from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post
# Create your views here.


class BlogListView(ListView):
    """Bu holatda view page hosil bo'ladi"""
    model = Post
    template_name = 'home.html'


class BlogDetailView(DeleteView):
    """Bu Pagega kirgaanda tolu malumotlar boladi """
    model = Post
    template_name = 'post_detail.html'
















