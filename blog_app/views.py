from django.shortcuts import render
from django.views.generic import TemplateView


class ListPostBlogView(TemplateView):
    template_name = "partials/blog/blog.html"
