from django.urls import path

from .views import ListPostBlogView

app_name = "blog_app"

urlpatterns = [
    path("list_post/", ListPostBlogView.as_view(), name='list_post_blog'),
]
