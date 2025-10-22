from django.contrib import admin
from .models import (
    Media,
    Comment,
    ReviewLike
)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(ReviewLike)
class ReviewLikeAdmin(admin.ModelAdmin):
    pass
