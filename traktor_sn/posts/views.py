from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('posts-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
