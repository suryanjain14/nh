from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news_update/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'news_update/post_detail.html'
