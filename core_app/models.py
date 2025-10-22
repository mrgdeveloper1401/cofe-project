from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.functional import cached_property


# Create your models here.
class CreateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdateMixin(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Media(CreateMixin, UpdateMixin):
    MEDIA_TYPE = [
        ("image", "تصویر"),
        ("video", "ویدیو"),
    ]
    # File & metadata
    user = models.ForeignKey("account_app.User", on_delete=models.PROTECT, related_name="user_media")
    file_type = models.CharField(max_length=10, choices=MEDIA_TYPE)
    image  = models.ImageField(
        upload_to='images/%Y/%m/%d/',
        help_text=_('Upload the original image file.'),
    )
    obj_file = models.FileField(upload_to="upload/file/%Y/%m/%d")
    image_id_ba_salam = models.BigIntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text=_('ID of the image in external storage')
    )
    is_active = models.BooleanField(_("is active"), default=True)

    @cached_property
    def get_image_url(self):
        return self.image.url

    class Meta:
        ordering = ("-id",)
        db_table = 'image'


class Comment(MPTTModel, CreateMixin, UpdateMixin):
    user = models.ForeignKey(
        "account_app.User",
        on_delete=models.PROTECT,
        related_name="user_comments"
    )

    # ارتباط عمومی به هر مدل (مثلاً Product یا PostBlog)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='children'
    )

    comment_body = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0)
    likes = models.ManyToManyField(
        "account_app.User",
        related_name="liked_comments",
        blank=True
    )
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['created_at']

    class Meta:
        db_table = 'comment'
        ordering = ('-id',)
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class ReviewLike(CreateMixin, UpdateMixin):
    review = models.ForeignKey(Comment, on_delete=models.PROTECT, related_name='review_likes')
    user = models.ForeignKey('account_app.User', on_delete=models.PROTECT, related_name="user_review_likes")
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        ordering = ("-id",)
        unique_together = ('review', 'user')
        db_table = "review_like"
