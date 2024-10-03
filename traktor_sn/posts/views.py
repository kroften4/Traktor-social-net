from django.shortcuts import render
from django.http import FileResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView
)
from .models import Post


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

    # unsanitazed user input
    # probably should restrict access to files other than etc/ and images/ in the future
    return FileResponse(open('images/' + imgname, 'rb'))
