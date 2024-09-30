from django.urls import path, re_path
from .views import PostListView, PostCreateView, get_image

urlpatterns = [
    re_path(r'^get_image/$', get_image),
    path('', PostListView.as_view(), name='posts-home'),
    path('post/new', PostCreateView.as_view(), name='post-create')
]
