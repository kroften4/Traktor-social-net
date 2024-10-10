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
    root = os.getcwd()
    traktor = os.path.normpath(os.path.join(os.getcwd(), "traktor_sn/"))
    path = os.path.abspath(os.path.join('images/', imgname))
    if not path.startswith(root):
        return HttpResponseNotFound("Error: attempted file access beyond top-level directory")
    if path.startswith(traktor):
        return HttpResponseNotFound("Error: File at that path not found")
    else:
        file = open('images/' + imgname, 'rb')
        return FileResponse(file)
