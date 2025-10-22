from django.db import models
from core_app.models import CreateMixin, UpdateMixin
from django.utils import timezone


class Coupon(CreateMixin, UpdateMixin):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    discount_type = models.CharField(max_length=10, choices=[("percent", "درصدی"), ("amount", "مبلغی")])
    value = models.DecimalField(max_digits=10, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    usage_limit = models.PositiveIntegerField(default=1)
    used_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("-id",)
        db_table = "coupon"

    def is_valid(self):
        return self.is_active and self.valid_from <= timezone.now() <= self.valid_to
