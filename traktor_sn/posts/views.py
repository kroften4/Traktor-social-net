from django.shortcuts import render
from .models import Post


# Create your views here.

def home(request):
    """
    Website main page with user-created posts
    """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/home.html', context)
