from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
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


class BlogCreateView(CreateView):
    """create"""
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    """Update template """
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeletView(DeleteView):
    """Delet qiladi """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home.html')





