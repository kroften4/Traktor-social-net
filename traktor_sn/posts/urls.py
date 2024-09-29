from django.urls import path, include
from .views import PostListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='posts-home'),
    path('post/new', PostCreateView.as_view(), name='post-create')
]
