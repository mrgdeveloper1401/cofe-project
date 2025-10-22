from django.db import models
from core_app.models import CreateMixin, UpdateMixin


from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Notification(CreateMixin, UpdateMixin):
    user = models.ForeignKey("account_app.User", on_delete=models.PROTECT, related_name="notifications")
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # برای اتصال به هر آبجکت دلخواه (مثلاً محصول یا سفارش)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        db_table = "notification"
        ordering = ("-id",)
