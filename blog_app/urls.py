from django.urls import path

from .views import (
    ListPostBlogView, 
    PostDetailDetailView
)

app_name = "blog_app"

urlpatterns = [
    path("list_post/", ListPostBlogView.as_view(), name='list_post_blog'),
    path("list_post/detail/<int:pk>/", PostDetailDetailView.as_view(), name='detail_blog_post')
]
