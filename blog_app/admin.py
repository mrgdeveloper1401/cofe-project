from django.contrib import admin
from .models import (
    CategoryBlog,
    PostBlog,
    PostBlogLikes,
    TagBlog
)


@admin.register(CategoryBlog)
class CategoryBlogAdmin(admin.ModelAdmin):
    pass


@admin.register(PostBlog)
class PostBlogAdmin(admin.ModelAdmin):
    pass    


@admin.register(TagBlog)
class TagBlogAdmin(admin.ModelAdmin):
    pass


@admin.register(PostBlogLikes)
class PostBlogLikesAdmin(admin.ModelAdmin):
    pass    
