from django.shortcuts import render
from django.http import FileResponse, HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView
)
from .models import Post
from pathlib import Path
import os

# Create your views here.

class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    extra_context = {'title': 'Home'}


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('posts-home')
    extra_context = {'title': 'New post'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts-home')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_mod


def get_image(request):
    """
    Includes path traversal vulnerability
    """
    # does not handle the case when imgname is not provided in request query
    imgname = request.GET.get('imgname')

    # "unsanitazed" user input
    root = os.path.abspath(Path(__file__).resolve().parents[2])
    traktor = os.path.normpath(os.path.join(root, "traktor_sn/"))
    path = os.path.abspath(os.path.join(root, 'images', imgname))
    if not path.startswith(root):
        return HttpResponseNotFound("Error: attempted file access beyond top-level directory")
    elif path.startswith(traktor) or not os.path.exists(path):
        return HttpResponseNotFound("Error: No such file or directory")
    else:
        file = open(path, 'rb')
        return FileResponse(file)
