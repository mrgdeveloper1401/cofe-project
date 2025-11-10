from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from blog_app.models import PostBlog


class ListPostBlogView(TemplateView):
    template_name = "partials/blog/blog.html"


# class PostDetailDetailView(DetailView):
#     model = PostBlog
#     template_name = "partials/blog/detail-post.html"

class PostDetailDetailView(TemplateView):
    template_name = "partials/blog/detail-post.html"
