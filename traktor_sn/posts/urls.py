from django.urls import path, re_path
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostDeleteView,
    get_image
)
from search.views import SearchView

urlpatterns = [
    re_path(r'^get_image/$', get_image),
    path('', PostListView.as_view(), name='posts-home'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]
