from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from treebeard.mp_tree import MP_Node
from django_ckeditor_5.fields import CKEditor5Field
from core_app.models import CreateMixin, UpdateMixin


class CategoryBlog(MP_Node, CreateMixin, UpdateMixin):
    category_name = models.CharField(max_length=255, db_index=True)
    category_slug = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    description_slug = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("-id",)
        db_table = "blog_category"


class TagBlog(CreateMixin, UpdateMixin):
    tag_name = models.CharField(max_length=255, db_index=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-id',)
        db_table = "blog_tag"


class PostBlog(CreateMixin, UpdateMixin):
    author = models.ManyToManyField('account_app.User', related_name='post_authors')
    category = models.ManyToManyField(CategoryBlog, related_name="blog_posts")
    post_title = models.CharField(max_length=255)
    post_slug = models.SlugField(max_length=500, allow_unicode=True)
    post_body = CKEditor5Field(config_name='extends')
    read_time = models.PositiveSmallIntegerField()
    post_cover_image = models.ForeignKey(
        "core_app.Image",
        on_delete=models.PROTECT,
        related_name="blog_posts_cover_image",
    )
    tags = models.ManyToManyField("TagBlog", blank=True, related_name="post_tags")
    likes = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    description_slug = models.TextField(blank=True, null=True)
    post_introduction = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        ordering = ("-id",)
        db_table = "blog_post"


class PostBlogLikes(CreateMixin, UpdateMixin):
    user = models.ForeignKey("account_app.User", verbose_name=_("user"), on_delete=models.PROTECT)
    post_blog = models.ForeignKey("PostBlog", verbose_name=_("post blog"), on_delete=models.PROTECT)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        ordering = ("-id",)
        db_table = "post_blog_likes"
