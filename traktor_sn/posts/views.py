from django.shortcuts import render
from django.http import FileResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
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


def get_image(request):
    """
    Includes path traversal vulnerability
    """
    imgname = request.GET.get('imgname')

    # unsanitazed user input
    # probably should restrict access to files other than etc/ and images/ in the future
    return FileResponse(open('images/' + imgname, 'rb'))
